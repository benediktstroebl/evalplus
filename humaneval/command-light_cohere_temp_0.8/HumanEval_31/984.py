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

This code defines a `is_prime` function that determines whether a given number is prime. It uses a specific rules to determine primality, such as checking for divisibility by 2 and 3, and then checking for divisibility by numbers within the square root of the input number.  The above implementation ensures that the function is self-contained and can pass all the tests for checking primality.