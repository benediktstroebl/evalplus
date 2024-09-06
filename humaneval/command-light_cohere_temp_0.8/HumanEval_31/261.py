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
This function takes an integer `n` as input and returns `True` if `n` is a prime number, and `False` otherwise. It uses a fact and some modular conditions to check if `n` is prime. The function then exhaustively checks all the primes up to the square root of `n` by testing divisibility with consecutive primes.