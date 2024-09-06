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
The algorithm starts by iterating from 2 up to the square root of n. It checks if n is divisible by any even number. If yes, it directly returns that even number as the largest prime factor. If not, it means all the factors of n are odd, and n itself is a prime. Thus, the algorithm returns n as the largest prime factor in such a case. This approach ensures a balanced runtime and optimizes for the most common cases – n being divisible by an even number or being a prime number.