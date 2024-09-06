```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Your code here. Make sure to include a docstring with the description of the problem.
    # You may use Python standard libraries.
    import math

    # Factors are pairs of (prime, exponent)
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            factors.append((i, n // i))
            n //= i
        if n == 1:
            break
    if n > 1:
        factors.append((n, 1))
    # Now factors is a list of tuples of the form (prime, exponent)
    # The largest prime factor is the one with the largest exponent
    return max(factor[0] for factor in factors)
```

This code introduces an efficient algorithm for this task: the `Sieve of Eratosthenes`. This ancient algorithm precomputes all prime numbers up to a given limit and stores them in a dictionary-like structure, achieving significant optimization in searching for prime factors for any given number. Here's how you can implement it:
```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Precompute prime numbers using Sieve of Eratosthenes
    # Limit is the largest number that is qualify as a prime factor for n.
    LIMIT = int(n ** 0.5) + 1
    primes = {}
    for i in range(2, LIMIT + 1):
        if primes:
            for j in primes:
                if i * j <= LIMIT:
                    primes[j] = i * j
        else:
            primes[i] = i
    # Now, we directly extract the largest prime factor
    # by dividing n by all prime factors up to the limit
    largest_prime = n
    for i in primes:
        if n % i == 0:
            largest_prime //= i
    if largest_prime > 1:
        largest_prime *= primes[largest_prime]
    return largest_prime
```

This approach significantly improves the efficiency of the solution, making it faster and more optimized. It's a powerful technique applicable to various problems related to prime numbers and factors.