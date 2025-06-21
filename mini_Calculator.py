# here is the mini scinetific caculator using python
# we will use built in module of math for our calculator
import math
import emoji 

print(emoji.emojize("📟 :red_heart:  Welcome to My Scientific Calculator :red_heart: 📟", language='alias'))

print(emoji.emojize("📜 Here is the Menu of our calculator", language='alias'))
print(emoji.emojize("🧠 Choose a number for further operations", language='alias'))

print('1.Addition')
print('2.Subtraction')
print('3.Multiplication')
print('4.Division ')
print('5.Square root')
print('6.Power (x^y)')
print('7.lograthim(log base 10)')
print('8.Sine')
print("9.Cosine")
print("10.Tangent")
 # taking a number as a choice from the user
choice=int(input('Please Enter any number(1-10): '))
 # if the user chooses for simple calculation
if choice in [1,2,3,4,6]:
  num1 = float(input('Please Enter a number: '))
  num2 = float(input('Please Enter the Second number: '))
elif choice in [5,7,8,9,10]:
 num= float(input("please enter a number: "))
else:
  print('Invalid Choice')
  exit()
print(emoji.emojize("\nResult:", language='alias'))

if choice == 1:
  print("sum of given two numbers is:",num1+num2)  
elif choice == 2:
  print("After  subtraction they give us :",num1-num2)
elif choice == 3: 
  print("Product of two numbers is:",num1*num2)
elif choice == 4:
  if num2 != 0:
    print("Quotient of thier division is",num1/num2)
  else:
    print("Division is not possible with zero (num/0) is not posssible")   
elif choice == 5:
  print('Square root is:',math.sqrt(num))    
elif choice == 6:
  print(num1,'raised to power of ',num2,'is',math.pow(num1,num2))  
elif choice == 7:
  print("log base 10 of ",num,'is',math.log10(num))  
elif choice == 8:
  print('sine of ',num,'is',math.sin(num)) 
elif choice == 9:
  print('Cosine of',num,'is',math.cos(num))
elif choice == 10:
  print('Tangent of ',num,'is',math.tan(num1)) 
print(emoji.emojize("\n💖 Thank you for using My Calculator. Stay smart", language='alias'))
 