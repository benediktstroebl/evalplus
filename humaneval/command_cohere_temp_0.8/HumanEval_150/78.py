Here's a Python script that contains the `x_or_y` function, which adheres to the problem statement:
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
    """Return x if n is prime, else return y."""
    if is_prime(n):
        return x
    else:
        return y

# Test cases
print(x_or_y(7, 34, 12))  # Output: 34
print(x_or_y(15, 8, 5))  # Output: 5
```

This script includes a `is_prime` function to validate if a number is prime, followed by the primary `x_or_y` function that uses this determination to decide which value to return. The test cases are included to verify the function's correctness.