Here is a Python script that defines a self-contained function to check if a number is a prime, and it passes all the tests provided:
```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check up to sqrt(n) to exclude 2 and 3
    sqrt_n = int(math.sqrt(n))
    for i in range(5, sqrt_n + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True
```

This script defines a function `is_prime` that checks if a given number `n` is prime. It uses a certain method to check for primality, which is simple and efficient for most cases.