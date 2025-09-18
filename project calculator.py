try:
   num1 = int(input("enter your first number: "))
   num2 = int(input("enter your second number: "))
   operator = input("which operator you want to select: ")


   if operator == "add":
    result = num1+num2
    print("sum is :", result)
   elif operator == "subtract":
    result = num1-num2
    print("difference is:", result)
   elif operator == "product":
    result = num1*num2
    print("product is:", result)

   elif operator == "division":
     result = num1/num2
     print("division is:", result)
   else:
    print("check again operator")
    
except ZeroDivisionError:
   print("you cannot divide with 0")
except ValueError:
   print("you have to only enter numeric values")