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
This code defines a function named `is_prime` that checks whether a given number is prime or not. The function uses an optimized algorithm that quickly tests for divisibility by only considering numbers within a certain range. It also incorporates checks for numbers that are less than or equal to 2 and 3, as they are definitely prime, and for odd numbers greater than 3, it uses a loop to efficiently check divisibility up to the square root of the number.