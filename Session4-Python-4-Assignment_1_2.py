# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 20:56:21 2018

@author: Ravikiran Bailkeri

Problem Statement 2:
Write a function filter_long_words() that takes a list of words and an integer n and returns the list
of words that are longer than n.
"""

def filter_long_words(string_, number):

    new_list = []
    #print(string_, number)
    for i in range(len(string_)):
       if (len(string_[i])) > number:
            new_list.append(string_[i])
    
    print (new_list)
            
list1 = input("String input: ")

list = list1.split(" ")

def main():
    global list, integer1
    integer = input("Enter NUmber: ")
    integer1 = int(integer)
    #print (list)
    filter_long_words(list, integer1)

main()