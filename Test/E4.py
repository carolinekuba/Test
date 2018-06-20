#!/usr/bin/python
# -*- coding: UTF-8 -*-
year = int(raw_input('Year:\n'))
month = int(raw_input('Month:\n'))
day = int(raw_input('Day: \n'))
months = [0,31,59,90,120,151,181,212,243,273,304,334]
if 0<month<=12:
    sum = months[month-1]
else:
    print "Wrong!"

sum += day
if(year %400 == 0)or ((year % 4 ==0) and (year % 100 !=0)):
    if month>2:
        sum += 1
print 'It is the %d day. '%sum

    
