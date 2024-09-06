```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Check for largest factor first which is not a prime
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
```
The function iterates through numbers from 2 to the square root of `n` and returns the largest one that divides `n` evenly. This works because larger factors come before smaller ones in the factorization of any number and prime factors are uncommon among large numbers. This solution is efficient and can solve large integer inputs within a reasonable time.