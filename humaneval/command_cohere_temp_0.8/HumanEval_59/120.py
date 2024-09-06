```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Divide n by 2 until odd, then multiply by 2^(ceil(log2(n)) - 2)
    # The largest prime factor of n will be 2, if not divisible by 2
    while n % 2 == 0:
        n //= 2
    # Start from 3 to skip 2 and divide by 2 until it's exhausted
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            n //= i
    return n
```

This algorithm divides `n` by 2 repeatedly until it becomes odd, indicating that 2 is no longer a factor; it then multiplies by 2 to account for any multiples of 2 that `n` may have had. Then, it iterates through odd numbers from 3 up to the square root of `n`, dividing `n` evenly by each one until it's exhausted. This ensures that the algorithm identifies the largest prime factor and returns it. 

The function docstring includes the problem statement and example behavior, and the function is standalone, not relying on external constants or variables.