#!/usr/bin/python
#coding=utf-8

import sys

"""
给定一个有序数组，例如: 1234555555789
寻找其中一个元素的最小下标和最大下标，例如: 
5的最小和最大下标是4,9
6找不到的结果就是-1,-1
"""

def find_begin(string, c):
    #print "string={s} c={c}".format(s=string, c=c)
    if len(string) == 0:
        return -1
    mid_i = len(string)/2
    mid = string[mid_i]
    #print "mid={m} mid_i={i}".format(m=mid, i=mid_i)
    if mid == c:
        begin = find_begin(string[0:mid_i], c)
        if begin == -1:
            begin = mid_i
    elif mid < c:
        begin = find_begin(string[mid_i+1:], c)
        if begin != -1:
            begin = mid_i + 1 + begin
    else:
        print "bug exist in find_begin: string={s} c={c}".format(s=string, c=c)
        sys.exit(1)
    return begin

def find_end(string, c):
    if len(string) == 0:
        return -1
    mid_i = len(string)/2
    mid = string[mid_i]
    if mid == c:
        end = find_end(string[mid_i+1:], c)
        if end == -1:
            end = mid_i
        else:
            end = mid_i + 1 + end
    elif mid > c:
        end = find_end(string[0:mid_i], c)
    else:
        print "bug exist in find_end: string={s} c={c}".format(s=string, c=c)
        sys.exit(1)
    return end

def find_both(string, c):
    print "string={s} c={c}".format(s=string, c=c)
    if len(string) == 0:
        return -1,-1
    mid_i = len(string)/2
    mid = string[mid_i]
    print "mid={m} mid_i={i}".format(m=mid, i=mid_i)
    if mid == c:
        begin = find_begin(string[0:mid_i], c)
        if begin == -1:
            begin = mid_i
        end = find_end(string[mid_i+1:],c)
        if end == -1:
            end = mid_i
        else:
            end = mid_i + 1 + end
        return begin,end
    elif mid > c:
        begin,end = find_both(string[0:mid_i], c)
        if begin == -1:
            return -1,-1
    elif mid < c:
        begin,end = find_both(string[mid_i+1:], c)
        if begin == -1:
            return -1,-1
        else:
            return mid_i + 1 + begin, mid_i + 1 + end
    return begin,end


print find_begin("1234555",'5')
print find_end("5556789",'5')
b,e = find_both("1234555555789", '5')
print (b,e)
assert (b,e) == (4,9)

print find_both("12345", '5')
print find_both("56789", '5')
print find_both("123346789", '5')

