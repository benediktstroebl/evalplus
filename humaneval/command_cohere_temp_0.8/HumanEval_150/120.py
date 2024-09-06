Here's a Python script that contains a function named `x_or_y` which returns either the value of `x` or `y` depending on whether the input `n` is a prime number or not:
```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def x_or_y(n, x, y):
    if is_prime(n):
        return x
    else:
        return y

# Test cases
print(x_or_y(7, 34, 12))  # This should print 34
print(x_or_y(15, 8, 5))  # This should print 5
```

This script works by first testing if the number is less than or equal to 3, as these numbers are trivially prime. If the number is greater than 3, it then checks whether it is divisible by 2 or 3, thus ruling out further possibilities. It then iterates through a series of numbers (starting from 5 and increasing by 6 each time), stopping once the square of the current number is greater than the input number. If the given number is divisible by any of the numbers encountered, it is not prime, and the `x_or_y` function returns the value of y. The function returns the value of x if the number is not divisible by any of the numbers checked, and is therefore prime. 

The above code defines the `is_prime` function that is used to test if a number is prime. The `x_or_y` function uses `is_prime` to determine whether to return x or y. The final two lines are examples that test the function. The first example should return 34 whereas the second example should return 5. These examples align with the examples provided in the prompt. 

This script will work as expected if the only import statement required is `import math`. Let me know if you would like any adjustments made to the script!