```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Seed with the second largest factor until a factor larger than it found or n becomes 1
    for potential_factor in range(n // 2 + 1, int(n ** 0.5) + 1):
        if n % potential_factor == 0:
            # If factorization is found, update n to its value and continue
            n //= potential_factor
        else:
            # If no factorization is found, this potential_factor is a prime factor
            # so return it
            return potential_factor
    # If no larger prime factor is found and n is not 1, then n is a prime
    # itself, so return n
    return n
```

The function iterates through potential factors from the second largest to the largest possible factor (sqrt(n)). If a larger factor is found, it is returned. Otherwise, the largest prime factor is the square root of n, a prime number itself. This approach ensures the function handles potential inputs of various sizes efficiently.