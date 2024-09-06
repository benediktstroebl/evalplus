Here is a Python script that provides a self-contained function to determine if a given number is a prime, and passes all the tests provided:
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

This code defines a simple and effective method to determine whether a given number is prime. It uses a specific rules and conditions to iteratively check for divisibility by numbers up to the square root of the number, ultimately returning True if the number is prime and False otherwise.