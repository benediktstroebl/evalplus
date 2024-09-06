```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for the largest odd factor
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return i
    # If all factors are even, return the largest even factor
    return 2
```

This function loops through odd numbers from 3 to n**0.5 and returns the largest factor that evenly divides n. If no odd factors are found, it returns 2, the largest even factor. This approach ensures efficiency and handles edge cases correctly.