```python
def is_prime(n):
    """Check if a number is prime."""
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
This Python function, `is_prime`, takes an integer `n` as input and returns `True` if `n` is a prime number, and `False` otherwise. It employs a necessary strategy of iterating up the square numbers that are less than or equal to the input number `n`, and checking for divisibility by 2, 3, and the square numbers. The function also uses a sieve of Eratosthenes to quickly identify the square numbers.