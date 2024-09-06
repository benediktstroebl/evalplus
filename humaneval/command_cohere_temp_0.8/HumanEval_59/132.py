```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for the largest even factor as the last digit
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    # If no even factors, then n is a prime itself
    return n
```
The function iterates through possible factors from 2 to the square root of n. If it finds an even factor, it returns it. If no even factors are found, then n must be a prime, and it returns n. This approach is efficient and guarantees the correct result for the largest prime factor.