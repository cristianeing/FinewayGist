#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 13:56:23 2018

@author: Cristian Eing
"""

words = open('data.txt','r').read().split()
words_seen = set()
word_count = {}
for word in words:
    if word in words_seen:
        word_count[word]+=1
    else:
        words_seen.add(word)
        word_count[word]=1
        
result = open("result.txt","w")
ordered_words = sorted(word_count,key=word_count.get,reverse=True)
for ordered_word in ordered_words:
    result.write(ordered_word+' ('+str(word_count[ordered_word])+')\n')
    
result.close()