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

# Example usage
print(x_or_y(7, 34, 12))  # This should print 34
print(x_or_y(15, 8, 5))  # This should print 5
```

This script includes a `is_prime` function that provides an efficient algorithm to determine if a number is prime or not. The `x_or_y` function uses this algorithm to determine whether to return the value of `x` or `y`. The two example usages are provided to demonstrate the function's behavior.