# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 17:57:19 2023

@author: Joseph Balbuena
"""
#PIN = 65875
#k = 1251625
count = 0

# count all the numbers between 1 and 10,000 (inclusive) that are even (divisible by 2)
for n in range(1,10_000+1):
  if (n % 2 == 0) or (n % 5 == 0) or (n % 6 == 0):
    count += 1

print(count)
