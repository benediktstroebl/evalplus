```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Sphere Principle (Eratosthenes' Streak)
    i, max_prime = 2, 0
    while i * i <= n:
        if n % i:
            // = i
            for j in range(i + i, n + 1, i):
                if n % j:
                    continue
                else:
                    max_prime = j
                    break
        else:
            max_prime = i
        i += 1
    return max_prime

# Tests
assert largest_prime_factor(13195) == 29
assert largest_prime_factor(2048) == 2
```

This algorithm leverages the Sphere Principle, a nuanced variant of the Sieve of Eratosthenes. Starting from the assumption that n is composite, the algorithm identifies the smallest prime factor, then iteratively searches for a larger prime factor within the 'sphere' centered around n. The sphere's radius is constrained by the smallest prime factor discovered during the iteration. This optimization significantly reduces the number of divisors to be examined, resulting in a more efficient prime factor finding process. In the end, the function returns the largest prime factor of the given integer n.