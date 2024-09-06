Here's a self-contained Python script that defines a function is_prime to determine if a given number is a prime:
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
This function, `is_prime`, takes an integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. It uses a proper strategy to determine primality, such as checking for divisibility by 2 and 3, then testing divisibility by numbers that can be expressed as 6n + k for k between 0 and less than n.

This function can be used to check for prime numbers in markdown code blocks to provide a solution to the problem.