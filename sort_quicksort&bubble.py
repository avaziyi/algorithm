# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 21:36:07 2013

@author: 子怿
"""

import random
import datetime
import copy

def quicksort(data, low = 0, high = None):
	if high == None:
		high = len(data) - 1
	if low < high:
		s, i, j = data[low], low, high
		while i < j:
			while i < j and data[j] >= s:
				j = j - 1
			if i < j:
				data[i] = data[j]
				i = i + 1
			while i < j and data[i] <= s:
				i = i + 1
			if i < j:
				data[j] = data[i]
				j = j - 1
		data[i] = s
		quicksort(data, low, i - 1)
		quicksort(data, i + 1, high)
	return data

def bubblesort(data):
	for i in range(len(data) - 1, 1, -1):
		for j in range(0, i):
			if data[j] > data[j + 1]:
				data[j], data[j + 1] = data[j + 1], data[j]
	return data

def sort_perfmon(sortfunc, data):
	sort_data = copy.deepcopy(data)
	t1 = datetime.datetime.now()
	sortfunc(sort_data)
	t2 = datetime.datetime.now()
	print sortfunc.__name__, t2 - t1
	#print sort_data

data = [random.randint(0, 100) for i in range(1000)]
#print data
sort_perfmon(quicksort, data)
sort_perfmon(bubblesort, data)
#print quicksort(data)
#print bubblesort(data)