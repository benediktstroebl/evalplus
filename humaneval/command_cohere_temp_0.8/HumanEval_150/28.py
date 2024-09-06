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
print(x_or_y(7, 34, 12))  # Output: 34
print(x_or_y(15, 8, 5))  # Output: 5
```

This script defines a function `x_or_y` that takes three arguments: `n` (which is checked for primality), and two values `x` and `y`, returning respectively `x` or `y` depending on the primality of `n`. The primality-checking mechanism involves a mixture of checks for small numbers and checks for divisibility by small primes. 

The script also includes test cases to help verify if the function `x_or_y` is working correctly. 

To ensure that the function `x_or_y` is self-contained and does not rely on global variables, it is recommended to keep the function definitions and tests within the same file but avoid declaring variables outside of functions or interacting with external resources.