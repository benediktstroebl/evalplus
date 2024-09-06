Here is a Python script that solves the problem of checking if a number is prime, and passes the tests provided:
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
This function uses an optimized trial division to determine whether a given number is prime or not. It returns True if the
number is prime and False otherwise. The function can also be tested with various test cases to ensure its correctness.