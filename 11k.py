##1
##from math import*
##бит=ceil(log2(250))
##ид=ceil(86*бит/8)
##отв=256*ид
##print(отв)


##2
##from math import*
##бит=ceil(log2(4090+10))
##ид=ceil(бит*101/8)
##отв=ид*2048/1024
##print(отв)

##3
##from math import*
##бит=ceil(log2(10+2040))
##ид=ceil(бит*56/8)##в байтах один ид
##юз1=125*1024/512
##отв=юз1-ид
##print(отв)

##4
##from math import*
##бит=ceil(log2(10+60))
##ид= ceil(бит*24/8)
##юз1=70*1024/2048
##отв=юз1-4-ид
##print(отв)

##5
##from math import*
##бит=ceil(log2(26+26+10))
##ид=ceil(12*бит/8)
##отв=20*1024/(28+ид)
##print(отв)

##6
##from math import*
##for l in range(1,1000):
##    bit=ceil(log2(10+52+500))
##    idd=ceil(bit*l/8)
##    if idd *45877 >= 49 *1024 *1024:
##        print(l)
##        break

##7
##from math import*
##for l in range(10000,1,-1):
##    bit=ceil(log2(10+52+1988))
##    idd=ceil(bit*l/8)
##    if idd*1974 <= 579 *1024:
##        print(l)
##        break

##8
##from math import*
##for abc in range(1,10000):
##    bit=ceil(log2(abc))
##    idd=ceil(bit*2783/8)
##    if idd* 3845627>=11*1024*1024*1024:
##        print(abc)
##        break

##9
##from math import *
##for abc in range(1000000,1,-1):
##    bit=ceil(log2(abc))
##    idd=ceil(bit*23/8)
##    if idd * 500000<=21*1024*1024:
##        print(abc)
##        break
##    

##10
##from math import*
##for spc in range(10000,1,-1):
##    bit=ceil(log2(26+26+10+spc))
##    idd=ceil(bit*24/8)
##    if idd*5100<=170*1024:
##        print(spc)
##        break

##11
##from math import*
##bit=ceil(log2(10+8190))
##idd=ceil(bit*303/8)
##us1=101*1024/101
##ans=us1-idd
##print(ans)

##12
from math import*
for i in range(100000,1,-1):
    bit=ceil(log2(10+999))
    idd=ceil(bit*745/8)
    user=idd+i
    if 312*user<=311*1024:
        print(312*i)
        break
