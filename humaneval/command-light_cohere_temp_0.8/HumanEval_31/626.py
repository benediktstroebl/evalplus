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
This function, `is_prime`, takes an integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. The function uses basic criteria to determine if a number is prime, such as `2` and `3` are prime numbers, as well as numbers that are divisible only by 2 and 3, or numbers that exceed a square root.