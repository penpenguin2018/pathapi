#!/usr/bin/env python
#coding:utf8
import sys
import re

path = "/project/circle/shot/FOO/0010/comp/FOO_0010_comp_v001.1001.nk"

def project(path):
	"""
	경로를 넣으면 project를 반환한다.
	"""
	p = re.findall('project/(\w+)', path.replace("\\", "/"))
	if len(p) != 1:
		return "", "경로에서 project 정보를 가지고 올 수 없습니다."
	return p[0], None

def seq(path):
	"""
	경로에서 seq 이름을 반환한다.
	"""
	p = re.findall('/shot/(\w+)', path.replace("\\", "/"))
	if len(p) != 1:
		return "", "경로에서 sep 정보를 가지고 올 수 없습니다."
	return p[0], None

def shot(path) :
	"""
	경로에서 shot 이름을 반환한다.
	"""
	p = re.findall('/shot/\w+/(\w+)', path.replace("\\", "/"))
	if len(p) !=1:
		return "", "경로에서 shot 정보를 가지고 올 수 없습니다."
	return p[0], None

def task(path) :
	"""
	경로에서 task 이름을 반환한다.
	"""
	p = re.findall('/shot/\w+/\w+/(\w+)', path.replace("\\", "/"))
	if len(p) !=1:
		return "", "경로에서 task 정보를 가지고 올 수 없습니다."
	return p[0], None

def ver(path):
	"""
	경로에서 ver 정보를 반환한다.
	"""
	p = re.findall('_v(\d+)', path.replace("\\","/"))
	if len(p) != 1 :
		return -1, "경로에서 ver 정보를 가지고 올 수 없습니다."
	return int(p[0]), None

def seqnum(path):
	"""
	경로에서 seqnum 정보를 반환한다.
	"""
	p = re.findall('\.(\d+)\.', path.replace("\\", "/"))
	if len(p) != 1 :
		return -1, "경로에서 seqnum 정보를 가지고 올 수 없습니다."
	return int(p[0]), None

if __name__ == "__main__":
	project, err = seqnum(path)
	if err:
		sys.stderr.write(err+"\n")
		sys.exit(1)
	print project
