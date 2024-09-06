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
    """Return x if n is a prime number, otherwise return y."""
    if is_prime(n):
        return x
    else:
        return y

# Test cases
print(x_or_y(7, 34, 12))  # Output: 34
print(x_or_y(15, 8, 5))  # Output: 5
```

This script defines a function `x_or_y` that takes three arguments: `n` (the number to examine), `x` (the value to return if `n` is prime), and `y` (the value to return if `n` is not prime). The function uses the `is_prime` function to determine whether `n` is prime and returns `x` or `y` accordingly.

The `is_prime` function is also included, which checks whether a given number is prime or not by iterating from 2 to the square root of the number and checking for divisibility. If the number is less than 2 or has any divisors between 2 and the square root, it's not considered prime.