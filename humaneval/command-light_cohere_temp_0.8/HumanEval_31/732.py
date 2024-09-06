```python
def is_prime(n):
    """Returns true if the number is prime, else false."""
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
This function `is_prime` returns `True` if the given number is prime, and `False` otherwise. The function uses a approach to identify prime numbers using trial and error, a method that attempts to find factors of the given number and checks for divisibility.  This following the In many cases, `is_prime` is a good solution to the problem.