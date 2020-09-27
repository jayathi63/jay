#!/usr/bin/python3
print("content-type:text/html")
print()
import cgi
import subprocess

form=cgi.FieldStorage()
cmd=form.getvalue("x")
print(cmd)

print(output)
if("date" in cmd):
	output=subprocess.getoutput("date")
elif("cal" in cmd):
	output=subprocess.getoutput("cal")













