```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Divide n by 2 until odd, then multiply by 3 (skipping odd multiples of 3)
    # Continue loop until multiplicative gap is less than or equal to 2
    for i in range(1, int(n ** 0.5) + 1):
        while not n % 2 and not n % 3:
            n //= 2
            if n == 1:
                return i
            n *= 3
    # If we reach here, n is a prime greater than 3
    return n
```