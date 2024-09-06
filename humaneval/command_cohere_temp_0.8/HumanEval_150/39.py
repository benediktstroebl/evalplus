Here's a Python script that contains the `x_or_y` function, followed by examples that show how the function works with different inputs:
```python
def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    """Return x if n is prime, otherwise return y."""
    if is_prime(n):
        return x
    else:
        return y

# Examples:
print(x_or_y(7, 34, 12))  # Output: 34
print(x_or_y(15, 8, 5))  # Output: 5
```

This script includes the `is_prime` function, which efficiently checks if a number is prime, and the `x_or_y` function that uses it to solve the problem as specified in the prompt. The examples at the bottom demonstrate the correct behavior of the `x_or_y` function.