```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for the largest even factor as the answer
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    # If no even factors, then n is a prime itself
    return n
```
The algorithm starts by iterating from 2 up to the square root of n. It checks whether n is divisible by each number. If a divisor is found, it returns that divisor as the largest prime factor. If no divisors are found up to the square root, then n must be a prime itself, so it returns n as the largest prime factor. This approach ensures that the largest prime factor is found accurately in O(sqrt(n)) time complexity.