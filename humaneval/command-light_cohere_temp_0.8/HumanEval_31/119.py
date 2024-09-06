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
The function checks for primality of a given number n. It returns True if the basic primality tests pass, and false otherwise. The function uses a simple logic to determine if a number is prime, without relying on any external functions or modules. It is self-contained and optimized for efficiency.