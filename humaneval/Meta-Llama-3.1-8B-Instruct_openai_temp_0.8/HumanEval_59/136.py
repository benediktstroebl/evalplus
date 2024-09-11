```python
def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

# Test cases
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script defines a function `largest_prime_factor` that takes an integer `n` as input and returns its largest prime factor. The function iterates from 2 to the square root of `n`, checks if `n` is divisible by the current number, and if it is, divides `n` by this number. This process continues until `n` is no longer divisible by any of the numbers in the range. At this point, `n` is a prime number, and since we're only interested in the largest prime factor, we return `n`.

Note: This solution uses a trial division approach, which is simple but not the most efficient for large numbers. For larger numbers, you might want to use a more advanced algorithm like the Sieve of Eratosthenes or the Miller-Rabin primality test.