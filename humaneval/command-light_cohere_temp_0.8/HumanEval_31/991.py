Here's the Python script with a self-contained function that checks if a given number is prime:

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

This script defines a function `is_prime` that checks if a given number `n` is prime. The function uses the strategy of checking divisibility up to the square root of `n` and quickly returns `True` if the number passes all tests. It also uses the prime numbers are the numbers greater than 1 that are divisible by 2 and 3, but not by any smaller numbers. The function then uses a classic Sieve of Eratosthenes algorithm to do this.

You can use this function to test and check for yourself if a number is prime or not.