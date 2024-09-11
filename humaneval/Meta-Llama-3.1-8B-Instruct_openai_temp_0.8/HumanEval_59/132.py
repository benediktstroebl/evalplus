```python
def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.

    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

# Test cases
print(largest_prime_factor(13195))  # Expected output: 29
print(largest_prime_factor(2048))   # Expected output: 2
```

This script uses a function to find the largest prime factor of a given number. It works by continuously dividing the number by the smallest divisor (starting from 2) until it can no longer be divided evenly, at which point the remaining number is the largest prime factor. If the number is not divisible by the current divisor, the divisor is incremented by 1. This process continues until the divisor is greater than the square root of the number, at which point the remaining number is the largest prime factor.