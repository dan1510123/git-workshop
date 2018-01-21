#!/usr/bin/env python

def fizzbuzz(n):
    for i in range(1,n+1):
        if i % 105 == 0:
            print("fizzbuzzbizz")
        elif i % 35 == 0:
            print("buzzbizz")
        elif i % 21 == 0:
            print("fizzbizz")
        elif i % 15 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        elif i % 7 == 0:
            print("bizz")
        else:
            print(i)
