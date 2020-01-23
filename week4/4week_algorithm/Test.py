import pandas as pd
import numpy as np
from Ban import Ban
from Student import Student
data = pd.read_csv("student.txt", delimiter=' ', header=None)

# 이름, 반 , 번호
# 각 요소별 접근 쉽게 하기 위해, numpy로 변환
data = np.array(data)

print(data)

Ban_list = []

for i in data:


    # Ban_list가 비어있으면, 새로 삽입
    if (len(Ban_list) == 0):
        Ban_list.append(Ban(i[1]))
    # 이미 Ban_list에 그 반이 들어가있으면 pass
    elif (Ban(i[1]) in Ban_list):
        pass
    else:
        Ban_list.append(Ban(i[1]))

    # 반과, sudent instance 생성.
    # Ban(i[1]).addlist(Student(i[2], i[0]))
    Ban_list[Ban_list.index(Ban(i[1]))].student_list.append(Student(i[2], i[0]))


Ban_list.sort()
for j in Ban_list:
    # 몇반, 몊명인지 print
    print(j, j.count_student(),"명")
    #반 class의 student_list 안에있는 Student class들 sort!
    j.student_list.sort()
    s_list=j.student_list
    for i in s_list:
        print(i)

