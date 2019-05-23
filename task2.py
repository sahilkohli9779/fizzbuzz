import os 

direc=input("Enter directory: ")
my_cmd='cd '+direc
result=os.system(my_cmd)
