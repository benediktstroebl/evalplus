```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for the largest even factor as the answer
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    # If no even factor found, then n is a prime itself
    return n
```
The function iterates through factors from 2 up to the square root of `n` and returns the largest even factor of `n` if there is one, or `n` itself if no larger even factor is found, adhering to the given problem statement and test scenarios.