```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Write n as 2^a * 3^b * 5^c * ... * p_m^d
    # Then return max(a, b, c, d, ...)
    exp = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            exp += 1
            while n % i == 0:
                n //= i
        if n == 1:
            return i
    return int(n)
```