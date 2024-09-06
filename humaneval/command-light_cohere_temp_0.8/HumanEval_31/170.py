Here is a self-contained Python function that solves the problem of checking whether a given number is a prime, and passes the corresponding tests:
```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
```

This function uses a simple algorithm to check for primality. It iterates through `i` until the square root of the number is greater than the number itself, or until the number is divisible by `i` or `i + 2`. It then checks if the number is divisible by any number in this range.