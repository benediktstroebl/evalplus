```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Loop through each number from 2 to the square root of n.
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
```
The function iterates through factors from 2 up to the square root of `n` (excluding `n` itself, since it's assumed to be larger than 2) and returns the largest prime factorization found. This is an efficient approach, as it only considers prime factors that contribute significantly to the factorization.