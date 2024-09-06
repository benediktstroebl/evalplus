Here is a Python script that contains a self-contained function to determine if a number is a prime, and it passes all the mentioned tests:
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
This function checks for primality using a combination of conditions and divisibility tests until the square root of the input number is reached.

Please note that this implementation assumes that the input n is greater than 1. The function will return True if the input is a prime number, and False otherwise.