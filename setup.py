#!/bin/python3
import sys

#Create database
#try:
from scripts import module_create_database
module_create_database.create()
#except:

#Create admin user
#try:
from scripts import module_add_admin
name = input("What is your admin name? ")
ip = input("What is your admin ip? ")
tg = input("What is your admin Telegram id? ")
config_name = input("What is your configuration file name? ")
print(module_add_admin.add(name+":"+ip+":"+tg+":"+config_name))
#except:
#	print("Error: cannot create admin")
#	sys.exit()

print("Installation completed")
