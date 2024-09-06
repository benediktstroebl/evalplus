Here's a Python script with a self-contained function that solves the x_or_y problem and passes the tests provided:
```python
def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
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

# Test Cases
print(x_or_y(7, 34, 12))  # Output: 34
print(x_or_y(15, 8, 5))  # Output: 5
```

This script defines a function `x_or_y` that takes three arguments: an input number `n`, and two values `x` and `y` that the function should return depending on whether `n` is prime or not. The script also includes a function `is_prime` to check if a given number is prime or not. The `x_or_y` function utilizes the `is_prime` function to control the flow of returning `x` or `y`. Finally, the script includes test cases to verify the functionality of the `x_or_y` function. 

Note: The `is_prime` function uses a simple optimization of checking divisibility by 2 and 3 separately, and then iterates from 5 to check for divisibility by any odd number, thereby covering most prime numbers. This allows the function to terminate sooner than a brute-force approach that checks all divisors.