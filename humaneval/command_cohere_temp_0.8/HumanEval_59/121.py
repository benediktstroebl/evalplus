```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Handle the case of n being a power of 2, which has no divisors besides 1 and itself
    if n == 2:
        return 2
    while n % 2 == 0:
        n //= 2
    # Check for oddness to filter out even numbers, except for 2, which was handled above
    if n % 2 == 1:
        return n
    # Divide n by odd numbers, increasing in steps of 2s until a prime is found
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            n //= i
    return n
```

This approach first checks if n is a power of 2, which has no prime factors besides 1 and itself. It then checks for oddness to filter out even numbers, except for 2, which is handled in the first step. Finally, it divides n by odd numbers increasing in steps of 2s until a prime is found. This approach is efficient because it quickly eliminates even numbers and progressively splits the search range for primes in halves.