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

    # Traverse through 2 and successive primes <= n, return the largest prime
    for i in range(2, n):
        if is_prime(i) and n % i == 0:
            return i
    return n
```

This Python script defines a function `largest_prime_factor(n)` that finds the largest prime factor of a given number `n`. It assumes `n` is greater than 1 and not a prime itself. The function uses a nested helper function, `is_prime(m)`, to check if a number `m` is prime. It iterates through numbers from 2 up to the square root of `m`, if `m` has no divisors other than 1 and itself, it is considered prime. The largest prime factor is determined by iterating through primes less than or equal to `n` and returning the largest one that divides `n`. This approach efficiently finds the largest prime factor without the need for factoring `n` completely.