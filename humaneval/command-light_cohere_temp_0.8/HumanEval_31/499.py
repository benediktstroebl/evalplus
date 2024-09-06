Here's a self-contained Python function that checks whether a given number is prime:
```python
def is_prime(n):
    """Returns true if the number is prime, false otherwise."""
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
This function, `is_prime`, takes an integer `n` as input and returns `True` if `n` is a prime number, and `False` otherwise. It uses some heuristic primality criteria and checks divisibility and basic divisors up to the square root of the number.

This function can be used to check whether a given number is prime, and it passes all the test cases provided in the original prompt.