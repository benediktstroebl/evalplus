Here's a Python script that contains a function named `x_or_y` that solves the problem:
```python
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    """Return x if n is prime, otherwise return y."""
    if is_prime(n):
        return x
    else:
        return y

# Tests
assert x_or_y(7, 34, 12) == 34
assert x_or_y(15, 8, 5) == 5
```

This code defines a function `x_or_y` that takes three arguments: an input number `n`, and two optional parameters `x` and `y`. The function will return `x` if the input `n` is prime, and `y` if n is not prime. The code also includes a unit test function, which checks if the `x_or_y` function works correctly for the given examples. 

The `is_prime` function is also included to validate if a number is prime or not. It can be used separately for other prime number-related operations if needed.