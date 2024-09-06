Here's the function `is_prime()` to determine if a given number is prime:
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
This function, `is_prime()`, takes a number `n` as input and returns `True` if `n` is a prime number and `False` otherwise. 

It uses a sieve of Eratosthenes algorithm to check for primality, by iterating up to the square of the number and checking if it's divisible by any number from 2 to the square root.