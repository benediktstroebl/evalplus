Here's a Python script that contains the defined function `x_or_y` that solves the problem:
```python
def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is a prime number and should return the value of y otherwise."""
    if is_prime(n):
        return x
    else:
        return y

# Test cases
print(x_or_y(7, 34, 12))  # Output: 34
print(x_or_y(15, 8, 5))  # Output: 5
```

This script defines a helper function `is_prime` that checks if a number is prime. The `x_or_y` function utilizes `is_prime` to determine whether to return `x` or `y`. The test cases are provided to demonstrate the function's correctness. Adjust the test cases to match your specific ones if needed.