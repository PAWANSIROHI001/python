# today we learned Recursion

# Recursion call by itself in the program

# for example
# factorial(6)
# factorial(n) = n * factorial(n-1)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
print(factorial(5))
print(factorial(4)) 