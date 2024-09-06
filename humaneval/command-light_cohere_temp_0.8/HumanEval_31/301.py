Here's a Python script that solves the problem of checking whether a number is prime, and passes the tests you provided:

```python
def is_prime(n):
    """Returns true if the number is prime, and false otherwise."""
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

This function checks whether a given number is prime, returning `True` if the number is prime, and `False` otherwise. The function uses a simple and efficient checks to determine primality. The checks reduce to a basic criteria for prime numbers, which are: `2` and `3` are prime, numbers greater than `5` that are divisible by `2` or `3` are not prime, and all other numbers are composite (meaning they can be expressed as the product of two integers).