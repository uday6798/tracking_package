# -*- coding: utf-8 -*-
"""
Created on Fri May 21 10:01:46 2021

@author: uday9
"""

def check_twice1(lst,elm):
    return lst.count(elm)>1
def check_twice2(lst,elm):
    return (elm in lst and elm in lst[lst.index(elm)+1:])
def check_twice3(lst,elm):
    c=0
    for x in lst:
        if x ==elm: c+=1
    return c
def check_twice4(lst,elm):
    try:
        lst.remove(elm)
        lst.remove(elm)
    except:
        return False
    return True