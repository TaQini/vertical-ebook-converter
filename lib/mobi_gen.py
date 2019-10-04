#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab

import os
from .mobi_convert import file_name

def kindelGen(file_dir, output_file):
    opf = ''
    mobi = ''
    for i in file_name(file_dir,'opf'):
        print(file_dir,i,output_file)
        if 'OEBPS' in i:
            opf=i
    cmd = 'kindlegen ' + opf + ' -o ' + output_file
    print(cmd)
    os.system(cmd)
    for i in file_name(file_dir,'mobi'):
        print(file_dir,i,output_file)
        mobi=i
    cp = 'cp ' + mobi + ' ' + file_dir + '.mobi'
    print(cp)
    os.system(cp)
    rm = 'rm -r ' + file_dir
    print(rm)
    os.system(rm)
