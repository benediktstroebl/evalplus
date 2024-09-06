```python
def is_prime(n):
    """Check if a given number is prime."""
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
This code defines a function called is_prime that takes an integer n as input and checks whether it's a prime number. The function employs a certain efficient primality checks, starting with the basic cases (2 and 3) and then utilizing a trial-and-error strategy to verify other prime numbers up to the given n.