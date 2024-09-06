Here's a Python script that contains a function named `x_or_y` that solves the problem as per the instructions provided:
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

This script will output:
```bash
34
5
```

The `is_prime` function is used to check if `n` is prime. The `x_or_y` function then returns the corresponding value based on this primality check.