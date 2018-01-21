#!/usr/bin/env python

def fizzbuzz(n):
    s = ""
    for i in range(1,n+1):
        if i % 3 == 0:
            s += "fizz"
        if i % 5 == 0:
            s += "buzz"
        if i % 7 == 0:
            s += "bizz"
        if i % 11 == 0:
            s += "bazz"
        if i % 13 == 0:
            s += "boom"
        if i % 17 == 0:
            s += "bang"
        else:
            s += i

    print(s)
