#Write a Python program that prints the numbers from 1 to 100. If the number is dividable by 3 print Fizz, if the number is dividable by 5 print Buzz instead of the number. If the number is dividable by 3 and 5 print FizzBuzz instead of the number.

for num in range(1,101):
 list1 = ''
 
 if num % 3 == 0:
    list1 = list1 + "Fizz"
 
 if num % 5 == 0:
    list1 = list1 + "Buzz"
 
 if num % 5 != 0 and num % 3 != 0:
    list1 = list1 + str(num)
 
 print(list1)