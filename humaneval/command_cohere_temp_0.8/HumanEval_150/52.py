Here's a Python script that contains a function named `x_or_y` which returns either the value of `x` or `y` depending on whether the input `n` is a prime number or not:
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

# Test cases
print(x_or_y(7, 34, 12))  # This should print 34
print(x_or_y(15, 8, 5))  # This should print 5
```

This script includes a `is_prime` function that checks if a number is prime. The `x_or_y` function uses this to decide whether to return `x` or `y`. The two example cases are included as assertions and should print the correct result.