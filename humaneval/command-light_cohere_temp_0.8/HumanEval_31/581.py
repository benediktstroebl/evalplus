```python
def is_prime(n):
    """Returns true if n is prime, false otherwise."""
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
This code defines a function is_prime that checks whether a given number n is prime. The function uses an optimized trial-by-error algorithm with modular divibility test and sqrt loop.