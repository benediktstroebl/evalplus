Here is a self-contained Python script that defines a function is_prime that checks if a given number is a prime number:
```python
def is_prime(n):
    """Returns True if the number is prime, and False otherwise."""
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
This script provides a function `is_prime` that checks whether a given number is prime or not. It uses a start checking for numbers less than or equal to 2 and 3, then checks divisibility by numbers up to the square root of the number being tested, and finally returns true if no divisors were found.