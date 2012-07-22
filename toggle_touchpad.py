#!/usr/bin/python
import subprocess

cmd = subprocess.Popen('synclient -l', shell=True, stdout=subprocess.PIPE)
for line in cmd.stdout:
	if 'TouchpadOff' in line:
		lhs, rhs = line.split('=', 1)
		if '1' in rhs:
			subprocess.Popen('synclient TouchpadOff=0', shell=True)
		else:
			subprocess.Popen('synclient TouchpadOff=1', shell=True)
		break


