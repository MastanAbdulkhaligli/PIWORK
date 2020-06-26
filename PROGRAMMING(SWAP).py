# This is a python code 
# Getting input from user
first_var=int(input("Please give a number as 1st variable (e.g. int a=1) :"))
second_var=int(input("Please give a number as 2nd variable (e.g. int b=2) :"))

# Swapping
first_var=first_var+second_var
second_var=first_var-second_var
first_var=first_var-second_var

#Printing
print("The value of the 1st variable: {}, The value of the 2nd variable: {}".format(first_var,second_var) )
