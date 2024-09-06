```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Go through each number from 2 to n, and check if n is divisible
    for i in range(2, n):
        if n % i == 0:
            return i
    # If no factors are found, n is a prime
    return n
```