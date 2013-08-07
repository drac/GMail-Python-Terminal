#!/usr/bin/env python
import sys
# Import smtplib for the actual sending function-------------------------------
import smtplib
#Import os for remove stored username and password-----------------------------
import os

try:
   input = raw_input
except:
   pass
 
# Importing the email modules
from email.mime.text import MIMEText

#Testing if he/she logged in---------------------------------------------------
try:
   open('log.txt')
except IOError as e:
  answer = input ("You have to LOGIN! Do you want to login (y/n) ?: ")
  if answer=="y":
  	#LOGIN Procedure---------------------------------------------------------------
	print ("\n|***LOGIN***|")
	username = input ("\n\nusername:")
	password = input ("password:")
	#Saving Username and Password--------------------------------------------------
	logw = open ('log.txt', 'w')
	logw.write(username)
	logw.write("\n")
	logw.write(password)
	logw.close()	
  else:
	exit()
 

logr = open ('log.txt', 'r')
username = logr.readline()
password = logr.readline()

print ("Welcome, ", username)
print ("\n|Main-Menu|\n")
print ("[1] Send G-MAil\n")
print ("[2] Exit\n")
print ("[3] LOGOUT & Exit\n")
answer = input ("Type [number] to select option: ")
if answer=="2":
	exit()
elif answer=="3":
	os.remove('log.txt')
	exit()
elif answer=="1":
	# Create a text/plain message--------------------------------------------------
	msg = MIMEText(input ("\n|MAIN TEXT|\n"))
	msg['Subject'] = input('Subject: ')
	msg['From'] = username
	msg['To'] = input('To: ')
 
	# Send the message via gmail SMTP server---------------------------------------
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.ehlo()
	s.starttls()
	s.login(msg['From'], password) 
 
	try:
   	# Python 3.2.1--------------------------------------------------------------
   		s.send_message(msg)
	except AttributeError:
   	# Python 2.7.2--------------------------------------------------------------
   		s.sendmail(msg['From'], [msg['To']], msg.as_string())
 
	s.quit()
else:
	print("ERROR TYPE A NUMBER THAT EXIST IN MENU!")
	exit()
