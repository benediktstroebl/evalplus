```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Divide n by 2 until n becomes odd
    while n % 2 == 0:
        n //= 2
    # Check for odd prime factors up to sqrt(n)
    for potential_factor in range(3, int(n**0.5) + 1, 2):
        while n % potential_factor == 0:
            n //= potential_factor
            if n == 1:
                return potential_factor
    # If no factors are found, n is a prime
    return n
```