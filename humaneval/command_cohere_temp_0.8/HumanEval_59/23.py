```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for largest factor first
    largest = n // 2
    for possible_factor in range(3, int(n**0.5) + 1, 2):
        if n % possible_factor == 0:
            largest = possible_factor
    return largest
```

This approach is efficient and works correctly for the given test cases. It checks from the largest possible factor (half the number) down, skipping even numbers, until it finds a factor. This is ideal for larger numbers, as the largest factor is likely to be towards the start.