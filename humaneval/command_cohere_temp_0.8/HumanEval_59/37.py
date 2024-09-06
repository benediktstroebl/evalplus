```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Check for edge cases: 2 and number <= 3
    if n == 2:
        return n
    if n <= 3:
        return 2
    
    # Elder's Algorithm to find the largest prime factor
    y = n - 1
    while y & 1 == 0:
        y //= 2
    for i in range(3, int(y**0.5) + 1, 2):
        while n % i == 0:
            y //= i
            if y == 1:
                return i
            n //= i
    if n > 1:
        return n

# Test Cases
assert largest_prime_factor(13195) == 29
assert largest_prime_factor(2048) == 2
assert largest_prime_factor(177) == 177
```

The function iterates through potential factors from `3` up to the square root of `y`, repeatedly dividing `n` and `y` by each potential factor. Once the inner loop concludes without finding a factor, `n` must be a prime larger than the square root of `y`. The maximum number of iterations can be `√n`, making the time complexity of this approach `O(√n)`.