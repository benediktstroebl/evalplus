Here's a Python script with a self-contained function that checks whether a given number is a prime, and passes all the tests:
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
This code defines a function `is_prime` that takes an integer `n` as input and returns `True` if `n` is a prime, and `False` otherwise. It uses some basic rules to determine if a number is prime, such as `2` and `3` are prime, and if `n` is divisible by any number from 2 to the square root of `n` (`n^2`), it returns `False`. The function also uses a while loop to check divisibility up to the square root of `n` by incrementing the loop by 6 each time, which is the approximate value of the next prime number.