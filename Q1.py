
def find_largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        largest = num1
    elif num2 >= num1 and num2 >= num3:
        largest = num2
    else:
        largest = num3
    return largest

num1 = float(input("Enter number: "))
num2 = float(input("Enter  number: "))
num3 = float(input("Enter  number: "))

largest = find_largest(num1, num2, num3)

print(format(num1, num2, num3, largest))