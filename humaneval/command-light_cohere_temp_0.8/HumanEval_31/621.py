Here's a self-contained Python function that determines whether a number is a prime, and it passes the tests you provided:
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
This function employs a "backtracking" method to check for primality. It iterates through prime numbers up if the number does not meet any of the primality criteria.