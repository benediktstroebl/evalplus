Here's a Python script with a self-contained function that solves the problem and passes the tests:
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
    """Return x if n is prime, else return y."""
    if is_prime(n):
        return x
    else:
        return y

# Test cases
print(x_or_y(7, 34, 12))  # Output: 34
print(x_or_y(15, 8, 5))  # Output: 5
```
This script defines a function `x_or_y` that takes three arguments: `n` (a given number), `x` (return value for prime `n`), and `y` (return value for non-prime `n`). The function uses the `is_prime` function to determine whether `n` is prime and returns `x` or `y` accordingly.

The `is_prime` function is also included to check if a number is prime. It iterates through numbers from 2 to the square root of `n`, checking for divisibility. If the number is divisible by any integer in this range, it's not a prime; otherwise, it is prime.