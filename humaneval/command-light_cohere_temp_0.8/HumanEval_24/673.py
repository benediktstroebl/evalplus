Here's the self-contained Python script that includes the function `largest_divisor(n)` which aims to find the largest divisor of a given integer `n` that leaves a remainder of 0:
```python
def largest_divisor(n: int) -> int:
    if n <= 1:
        return n
    
    # Prime factorization using optimized Sieve of Eratosthenes
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * 2, n + 1, p):
                primes[i] = False
        p += 1
    
    # Largest divisor found by removing multiples of prime divisors
    largest_divisor = n - (sum(primes[p] for p in range(2, n+1)) + 1)
    return largest_divisor
```
This code implements an optimized version of prime factorization and uses the Sieve of Eratosthenes to quickly identify prime numbers.