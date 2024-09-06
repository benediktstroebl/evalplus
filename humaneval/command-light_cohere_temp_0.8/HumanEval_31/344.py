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
The function checks for primality by testing divisibility from 2 up to the square root of the number. It also tests a fact-checking against consecutive odd numbers, which are frequently used as a quick primality test. The function efficiently determines whether a number is prime or not, passing the tests.