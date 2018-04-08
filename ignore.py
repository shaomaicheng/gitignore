#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
import os
args = sys.argv
root_dir = ''
if len(args) < 2:
    print u'需要指定工程目录'
    exit(1)
elif len(args) > 2:
    print u'命令行参数不正确'
    exit(1)
else:
    print u"开始添加git ignore"
    root_dir = args[1]


file_uri = root_dir + '/.gitignore'
print 'gitignore文件目录为: ' + file_uri

file_isexist = os.path.exists(file_uri)
# print file_isexist

if file_isexist:
    # 文件存在
    os.system('rm ' + file_uri)

f = open(file_uri, 'w')

ignore_tup = ('/.idea/', '*.iml', '.gradle', '/local.properties', '/build', '.DS_Store', '.externalNativeBuild')
try:
    for it in ignore_tup:
        f.write(it)
        f.write('\n')
finally:
    f.close()

print u'gitignore添加完毕'
