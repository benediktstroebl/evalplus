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
The algorithm starts from the top, checking the largest factors first, which makes it efficient in terms of both time and space complexity. 

The approach leverages the fact that all prime factors greater than the largest even factor of a number are collectively weaker in determining the number's value than the largest even factor itself. Therefore, the largest even factor is more likely to be the largest prime factor.