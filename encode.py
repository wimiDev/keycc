#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import os

curpath = os.getcwd()

secpath = "\\string\\" #明文文件夹

keyspath = curpath + secpath + "key.ky" #key文件

keyfile = open(keyspath, "r")

content = keyfile.read()
print content

keyfile.close()