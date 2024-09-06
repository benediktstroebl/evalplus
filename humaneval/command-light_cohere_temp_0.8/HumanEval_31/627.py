Here is a Python script with a self-contained function that checks whether a given number is a prime:
```python
def is_prime(n):
    """Returns true if n is prime, and false otherwise."""
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
This script provides a function `is_prime` that takes an integer `n` as an argument and returns `True` if `n` is a prime number, and `False` otherwise. It uses some of the essential criteria for prime numbers, such as `2` and `3`, divisibility by squares and divisibility by consecutive odd numbers up to the square root of `n`. This function passes all the tests provided in the initial prompt.