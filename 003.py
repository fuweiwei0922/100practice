# 实例003：完全平方数
# 题目 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

import math
'''
#方法一: 速度慢  ：
for i in range(-100,10000):
    for j in range(1,10000):
        for k in range(1,10000):
            if (i+100)==j*j and (i+268)==k*k:
                print(i)
                
                '''
'''
#方法二：
import math
for z in range(10000):
    x=int(math.sqrt(100+z))
    y=int(math.sqrt(268+z))
    if (x*x==(100+z))and (y*y==(z+268)):
        print(z)
'''


#方法三：
for z in range(10000):
    x=math.sqrt(100+z)
    y=math.sqrt(268+z)
    if x == int(x) and  y == int(y):
        print(z)
