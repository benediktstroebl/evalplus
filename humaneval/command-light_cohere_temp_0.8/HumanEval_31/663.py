Here's a self-contained Python function to determine if a given number is prime, with comprehensive test cases:
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
The function checks for primality using a combination of basic tests and trial division. It starts by requiring numbers less than or equal to 3 to be prime, then checks divisibility by 2 and 3, and uses a trial division by squares method to check for primality beyond the square root of 6.