Here's a Python script with a self-contained function that solves the x_or_y problem and passes the tests provided in the markdown code block:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    if is_prime(n):
        return x
    else:
        return y

# Example usage
print(x_or_y(7, 34, 12))  # Output: 34
print(x_or_y(15, 8, 5))  # Output: 5
```

This script includes a helper function `is_prime` that checks if a number is prime. The `x_or_y` function uses this helper to decide whether to return `x` or `y`. The two example usages at the bottom demonstrate that the function returns the expected values for the given inputs.