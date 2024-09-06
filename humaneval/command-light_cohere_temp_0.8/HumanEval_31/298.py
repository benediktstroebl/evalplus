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
This code defines a function `is_prime` that checks whether a given number is prime. It uses a specified formula to check for primality, and the function returns `True` if the number is prime and `False` otherwise. The function also passes the various test cases for primality and correctly identifies the prime numbers.