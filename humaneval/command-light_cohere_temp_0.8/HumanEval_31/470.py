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
This code defines a function named `is_prime` that checks whether a given number `n` is prime or not. It employs several statistical tests to determine prime numbers and returns `True` if the number is prime and `False` otherwise. The function also includes some initial simple checks for small prime numbers and returns early if the number is less than or equal to 3.