def simple():
    num1 = 4
    num2 = 3
    sum = num1+num2
    subtraction = num1-num2
    multiply = num1*num2
    division = num1/num2
    modd = num1 % num2
    # Outputs
    print(sum)          # Sum
    print(subtraction)  # Subtraction
    print(multiply)     # Multiplication
    print(division)     # Division
    print(modd)         # Modd

simple()
print("")
print("")
print("")
# Sum


def sum(num1, num2):
    sum = num1+num2
    print("The Sum is : " + str(sum))


# Subtraction
def sub(num1, num2):
    sub = num1-num2
    print("The Subtraction is : " + str(sub))

# Multiplication


def multiply(num1, num2):
    multiply = num1*num2
    print("The Multiplication is : " + str(multiply))


# Division
def division(num1, num2):
    division = num1/num2
    print("The Division is : " + str(division))

# Modulus


def mod(num1, num2):
    mod = num1 % num2
    print("The Modulus is : " + str(mod))


num1 = int(input("Enter your 1st number : "))
num2 = int(input("Enter your 2nd number : "))

sum(num1, num2)
sub(num1, num2)
multiply(num1, num2)
division(num1, num2)
mod(num1, num2)

