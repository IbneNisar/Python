#Code snippets to teach kids Python with simple labs-- Munib
#April 19, 2020 
#Use the following code snippets to introduce the concepts of input/output, 
#conditional statements (if/else) & iterations (while loop)

name=input("What is your name?")
print("Hello " + name)

#------------------------------Snippet 1----------------------------------
#Import datetime package - tech the concept of reusable libraries available
import datetime
now = datetime.datetime.now()
print(now)
print(now.hour)
print ("Timestamp : ", now.year, now.month, now.day, now.hour, now.minute, now.second)


#------------------------------Snippet 2----------------------------------
#Teach if/else constructs by building upon last week lecture
if now.hour < 12:
    print("Good Morning, ", name)
elif now.hour < 20:
    print("Good Afternoon, ", name)
else: 
    print("Good Evening, ", name)

#------------------------------Snippet 3----------------------------------
# Add two numbers
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
print("The sum of these two numbers is : " + str(num1+num2))

###################  LAB  #####################
#Practice type casting / conversion between integer & string
#Repeat the above logic by inputting num1 and num2 into string variables
#But convert to integers at the time of addition.
################################################

#------------------------------Snippet 4----------------------------------
# Ask students to do multiplication and division & discuss Division "/" , Floor division "//" and Modulus "%"
num1 = input("Enter first number:")
num2 = input("Enter second number:")
result = int(num1)/int(num2)
print(num1 + " divided by " + num2 + "=" + str(result))

###################  LAB  #####################
#Ask students to try different operations using // and % and then discuss with class
################################################


#------------------------------Snippet 5----------------------------------
#Introduce iterations - Start with While loop.
#Input a number and then reverse count & print till 0
count = int(input("Enter a number for reverse count"))
while (count>0):
    print(count)
    count=count-1

###################  LAB  #####################
#Check if user entered a -ve number. If so, print an error message and exit
################################################


#------------------------------Snippet 6----------------------------------
#Following snippet asks for a number and prints multiplications facts for the number from 1 upto 12
number = int(input(" Let's create multiplication table. Enter a number from 2 to 10 "))
if number<2:
    print(" You entered a number less than 2. Good bye! ")
elif number>10:
    print(" You entered a number greater than 10. Good bye! ")
else:
    loop=1
    while (loop<=12): 
        print(str(number) + " x " + str(loop) + "="+ str(number*loop))
        loop=loop+1

#------------------------------Snippet 7----------------------------------
#Let's import another package for some fun
#Open a command prompt and run "pip install emoji" command, to download & install emoji module from internet
import emoji
print("\N{winking face}")
print(emoji.emojize(":winking_face_with_tongue:"))
print(emoji.emojize(":grinning_face_with_big_eyes:")) 
print(emoji.emojize(":zipper-mouth_face:")) 
