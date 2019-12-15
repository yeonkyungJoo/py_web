# 작업 디렉토리 변경
# import os

# # Get the current working directory
# currentPath = os.getcwd()
# print(currentPath) # C:\study\git\py_web

# # change path
# os.chdir(currentPath+'\PYTHON_BASIC')
# print(os.getcwd())

# Section11
# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv

import csv

# 예제1
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)
    # header 스킵
    next(reader)
    
    # 확인
    print(reader) # <_csv.reader object at 0x000002219C355048>
    print(type(reader)) # <class '_csv.reader'>
    print(dir(reader)) # '__iter__'
    print()

    for c in reader :
        print(c)

# 예제2
with open('./resource/sample2.csv', 'r') as f:
    reader = csv.reader(f, delimiter = '|')
    # header 스킵
    next(reader)
    
    # 확인
    # print(reader)
    # print(type(reader))
    # print(dir(reader)) 
    # print()

    for c in reader :
        print(c)

# 예제3 (Dict 변환)
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)

    for c in reader :
        # print(c)
        for k, v in c.items() :
            print(k, v)
        print('------------------')