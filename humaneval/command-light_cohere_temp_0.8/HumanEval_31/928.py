Here's a self-contained Python function that checks whether a given number is prime or not:

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

This function uses a combination of small prime numbers and sqrt(n) tests to efficiently determine whether the number is prime or not. 

It iterates through potential divisors in increments of 6, performing tests for odd divisors up to the square root of the number, and reducing the range of tests as the number gets larger.