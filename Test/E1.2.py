#!/usr/bin/python
# -*- coding: UTF-8 -*-

d=[]
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if(a!=b) and (a!=c) and (b!=c):
                d.append([a,b,c])

print "Total: ",len(d)
print d
