```python
def is_prime(n):
    """Returns True if the number is prime, False otherwise."""
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
This code defines a function `is_prime` that checks whether a given number is a prime or not. It uses some basic criteria along the basic prime numbers and some common factor tests. The function returns `True` if the input `n` is a prime, and `False` otherwise.