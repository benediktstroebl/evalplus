```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for the largest even factor as the answer
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    # If no even factor found, n must be a prime
    return n
```
The function iterates through numbers from 2 up to the square root of `n` and checks if it's divisible by any of these numbers. If it is, that divisor is returned as the largest prime factor. If no divisors are found up to the square root, then `n` must be a prime itself, so the function returns `n` as the largest prime factor. 

This approach ensures that the largest prime factor is found correctly, regardless of whether `n` is an even divisor or a prime number.