#Calculator in python 
#Function to add two numbers

def add(a,b):
 return a + b
#Function to subtract two numbers
def subtract(a,b):
 return a - b
#Function to multiply two numbers
def multiply(a,b):
 return a * b
#Function to divide two numbers
def divide(a,b):
 if b == 0:
  print("Error! Division by zero is not allowed.")
 else:
  return a / b
#Main function
def main():
 num1 = float(input("Enter first number: "))
 num2 = float(input("Enter second number: "))
 operation = input("Choose an operator (+,-,*,/): ")
 if operation == '+':
  result = add(num1,num2)
 elif operation == '-':
  result = subtract(num1,num2)
 elif operation == '*':
  result = multiply(num1,num2)
 elif operation == '/':
  result = divide(num1,num2)
 else:
  print("Invalid operator")
  
print("%.2f %s %.2f = %.2f" % ( num1 ,operation ,num2 , result ))
main()
#Calling the Main Function
if __name__=="__main__":
 main()


