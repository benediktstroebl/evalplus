Here's a Python script with a self-contained function that solves the x_or_y problem and passes the tests:
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

# Example usage
print(x_or_y(7, 34, 12))  # Output: 34
print(x_or_y(15, 8, 5))  # Output: 5
```

This script includes a `is_prime` function that checks if a given number is prime and the `x_or_y` function that returns the corresponding values based on whether the input number is prime or not. The example usage demonstrates the function's behavior for different inputs.