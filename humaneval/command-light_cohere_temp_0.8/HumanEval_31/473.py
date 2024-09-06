Here is a Python script that is self-contained with a function that solves the problem you provided:
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
This function uses a simple algorithm to determine if a number is prime. It starts by checking numbers less than or equal to 2 and 3, as these are known prime numbers. It then uses a mathematical fact to iteratively check divisibility by numbers that are the form of consecutive primes ending in 6.