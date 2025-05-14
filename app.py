first_number = 0
second_number = 0
result = 0
first_number = int(input("please enter the first number:"))
second_number = int(input("please enter the second number:"))
operation = input("please choose one of the following(+,-,*,/,%,pow)")

if operation == "+":
    result = first_number + second_number
elif operation == "-":
    result = second_number - first_number
elif operation == "*":
    result = first_number * second_number
elif operation == "/":
    result = first_number / second_number
elif operation == "%":
    result = first_number % second_number
elif operation == "pow":
    result = pow(first_number , second_number) 
else:
    print("error")

print("The result is:" , result)

