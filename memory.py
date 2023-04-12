import psutil
import time

import time
import sys
from colorama import Fore

print('RAM MEMORY :')

def display_usage(mem_usage):
    
    a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t = '  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  '
    if mem_usage > 5 :
        a = '##'
    if mem_usage > 10 :
        b = '##'
    if mem_usage > 15 :
        c = '##'
    if mem_usage > 20 :
        d = '##'
    if mem_usage > 25 :
        e = '##'
    if mem_usage > 30 :
        f = '##'
    if mem_usage > 35 :
        g = '##'
    if mem_usage > 40 :
        h = '##'
    if mem_usage > 45 :
        i = '##'
    if mem_usage > 50 :
        j = '##'
    if mem_usage > 55 :
        k = '##'
    if mem_usage > 60 :
        l = '##'
    if mem_usage > 65 :
        m = '##'
    if mem_usage > 70 :
        n = '##'
    if mem_usage > 75 :
        o = '##'
    if mem_usage > 80 :
        p = '##'
    if mem_usage > 85 :
        q = '##'
    if mem_usage > 90 :
        r = '##'
    if mem_usage > 95 :
        s = '##'
    if mem_usage > 98 :
        t = '##'
    
    print(f'\r['+a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+']',mem_usage,end='\r')

while True:
    display_usage(psutil.virtual_memory().percent)
    time.sleep(1.1)