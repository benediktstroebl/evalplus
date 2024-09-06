```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for the largest possible factor numerically
    largest_factor = n // 2
    while largest_factor > 1:
        if all(n % i for i in range(3, int(largest_factor ** 0.5) + 1, 2)):
            break
        largest_factor //= 2
    else:
        return n // 2  # Largest factor is n itself, a special case
    # Iterate through possible factors from 2 to largest_factor
    for i in range(2, largest_factor):
        if n % i == 0:
            return i
    return n  # This case should never happen
```

The approach works by first dividing `n` into halves until a candidate factor is found, then proceeding with divisibility checks from 2 up to that candidate factor. This strategy efficiently finds the largest prime factor while avoiding redundant checks.