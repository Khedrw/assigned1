#first project
a = int(input("Hi user, Enter your age "))
if a <= 5 :
 print(" the ticket is for free ")
elif a <= 12 :
 print (" The ticket price is $5 ")
elif a <= 18:
 print (" The ticket price is $7 ")
else:
 print (" The ticket price is $10 ")

 #second project
a = float(input("Hi user, Enter a number "))
if a % 2 == 0 :
    print("the number you enter it is even ")
else:
    print ("the number you enter it is odd ")

#third project
a = input ('please enter your name ')
b = input (' please enter your password ')
if a == "admin" and b == "1234" :
    print ('Access granted')
else:
    print ("Access denied")