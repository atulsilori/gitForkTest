def add(num1, num2):
    number1 = num1
    number2 = num2
    return number1+number2

def multiply(num1, num2):
    number1 = num1
    number2 = num2
    return number1*number2    

num1 = int(input("enter number1 >> "))
num2 = int(input("enter number2 >> "))
Sum = add(num1, num2)
mult = multiply(num1, num2)
print("sum is - ", Sum)
print("multiplication is - ", mult)
