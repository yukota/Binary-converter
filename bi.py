#! /usr/bin/env python
# -*- coding: utf-8 -*-

####################
#2進変換
####################
def prc_bi(iInput):
	#シフト演算用
	iShift =1	
	#list
	lstAns = []
	while iInput-iShift > 0:
		if (iInput & iShift) >0:
			print "1"
			lstAns.append(1)
		else:
			print "0"
			lstAns.append(0)
		
		iShift = iShift << 1
			
	print "test end"
	lstAns.reverse()
	print lstAns
	return lstAns
	
