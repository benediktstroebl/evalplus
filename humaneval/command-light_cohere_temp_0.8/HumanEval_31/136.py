Here is a Python script with a self-contained function that solves the problem of checking whether a given number is prime or not, and passes the tests:
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
The `is_prime` function takes an integer `n` as input and returns `True` if the number is prime, and `False` otherwise. It uses some basic primality criteria, checks divisibility by 2 and 3, and then employs a "6n" sieve to filter out all other potential divisors less than the square root of `n`. 

This function is self-contained and can be used to quickly determine whether a given number is prime or not, which can be very useful in a variety of applications.

You can also take this example further and modify it to incorporate more prime testing criteria or add extra features depending on the particular use case.