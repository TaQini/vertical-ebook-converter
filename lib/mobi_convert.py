#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab

import os
import io

def alter(file,old_str,new_str):
    file_data = ""
    with io.open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str,new_str)
            file_data += line
    with io.open(file,"w",encoding="utf-8") as f:
        f.write(file_data)

def alter_line(file,target_str,new_str):
    file_data = ""
    with io.open(file, "r", encoding="utf-8") as f:
        for line in f:
            if target_str in line:
                line = new_str+'\n'
            file_data += line
    with io.open(file,"w",encoding="utf-8") as f:
        f.write(file_data)

def alter_add(file,new_str):
    file_data = ""
    with io.open(file, "r", encoding="utf-8") as f:
        file_data = f.read()
        file_data += '\n'
        file_data += new_str
    with io.open(file,"w",encoding="utf-8") as f:
        f.write(file_data)

def file_name(file_dir,file_type): 
    L=[] 
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            # get files by file type
            if os.path.splitext(file)[1] == '.'+file_type:
                L.append(os.path.join(root, file))
    return L

def mobiConvert(file_dir = './'):
    for i in file_name(file_dir,'xhtml'):
        print(i)
        alter(i,'“','「')
        alter(i,'”','」')
        alter(i,'‘','『')
        alter(i,'’','』')
    for i in file_name(file_dir,'opf'):
        print(i)
        print('convert horizontal-lr to vertical-rl ...')
        alter(i,'horizontal-lr','vertical-rl')
        alter_line(i,'<dc:language>','<dc:language>zh-tw</dc:language>')
    for i in file_name(file_dir,'css'):
        print(i)
        text = 'body{\n\tmargin: 5%;\n\ttext-align: justify;\n\t-webkit-writing-mode: vertical-rl;\n}\n'
        print('added css: ')
        print(text)
        alter_add(i,text)
