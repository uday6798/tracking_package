# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 15:04:25 2021

@author: uday chowdary adusumilli
"""

from flask import Flask, request
import nlpmodel
import spacy
import dbmodel
import en_core_web_sm
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def startup():
    # create html skeleton
    html_question = '<html><title>FIQS</title><body><center><H1><em>T R A C K  &nbsp &nbsp A N A L Y Z E R</em></H1> \
    <H2><em>Fleet Information Query System</em></H2> \
    <form action = "http://localhost:5000/" method="post"  \
    <p>Submit query :  \
    <input type = "text" size=50 name="quest" />  \
    <input type = "submit" value="submit" /></p>  \
    </form></center></body></html>'
    # when user clicks submit button or enter key
    if request.method == 'POST':
        # create html table skeleton
        style = '<style>table th, td {border:1px solid black; border-collapse:collapse;} \
                th, td {padding: 4px; text-align:left;} </style>'
        # convert user question to sql query
        sqltext = nlpmodel.convert_text_sql(request.form['quest'])
        table = '<table style=width:50%><caption><H4>' + 'Your Query >>>> &nbsp <i>' + request.form[
            'quest'] + '</i></H4></caption>'
        #print(sqltext)
        # send sql query to db and receive the query execution output
        result_set, column_names = dbmodel.sql(sqltext)
        #print(result_set)
        # build table header and data rows for the sql output
        if result_set != None and len(result_set) > 0:
            table_columns = '<tr bgcolor="#BBBBBB">'
            for k in column_names:
                table_columns = table_columns + '<th>' + k.upper() + '</th>'
            table_header = table_columns + '</tr>'
            table_data = ''
            for row in result_set:
                
                table_data = table_data + '<tr>'
                for c in range(len(column_names)):
                    if row[c] == None:
                        table_data = table_data + '<td>' + "NA" + '</td>'
                    else:
                        table_data = table_data + '<td>' + str(row[c]) + '</td>'
                table_data = table_data + '</tr>'
            table_data = table_data + '</table>'
            return html_question + '<center>' + style + table + table_header + table_data + \
                '</center></body><style>.footer {position: fixed; bottom: 0; text-align: center;} </style><div class="footer"><p>....</p></div></html>'
        else:
            return html_question + '<center>' + style + table + \
                '</center></body><style>.footer {position: fixed; bottom: 0; text-align: center;} </style><div class="footer"><p>...</p></div></html>'

    return html_question

if __name__ == '__main__':
    app.run(debug=False)

# <style>.footer { position: fixed; bottom: 0; text-align: center;} </style>