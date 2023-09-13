def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Test the function
number = int(input("Enter a non-negative integer: "))
if number < 0:
    print("Factorial is undefined for negative numbers.")
else:
    result = factorial(number)
    print(f"The factorial of {number} is {result}")
