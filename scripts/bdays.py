#!/bin/python
import random

amount = int(input("Number of birthdays to generate: "))

x = 0
while x < amount:
	day = random.randint(1, 31)
	month = random.randint(1, 12)
	print(f'{month}-{day}')
	x+=1