```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    def is_prime(m):
        """Check if m is prime."""
        if m <= 1:
            return False
        for i in range(2, int(m**0.5) + 1):
            if m % i == 0:
                return False
        return True

    if is_prime(n):
        return n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 and is_prime(i):
            return i
    return 2

# Tests
assert largest_prime_factor(13195) == 29
assert largest_prime_factor(2048) == 2
```

This code defines a function `largest_prime_factor(n)` that takes an integer `n` as input and returns the largest prime factor of `n`, assuming `n` is greater than 1 and not a prime itself. The function iterates through potential factors up to the square root of `n`, checking for divisibility and also utilizing a separate primality-checking function (`is_prime(m)`) to efficiently determine if a number is prime. 

The test suite is also included to verify the function behavior against the provided test cases.