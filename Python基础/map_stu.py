# -*- coding: utf-8 -*-
# @Time    : 2018/10/19 9:15
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : map_stu.py
# @Software: PyCharm

# 普通
def fun(x):
    return x * x
print(list(map(fun, [1, 2, 3])))

# lambda
print(list(map(lambda x: x*x, [1, 2, 3])))

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

