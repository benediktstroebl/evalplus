```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return max(factors)
```
This approach optimizes the prime factorization process by iterating only up to the square root of `n`. For larger `n`, the factorization is performed only for multiples of 2 and odd numbers, reducing the number of iterations required. This improves efficiency while still ensuring the correct largest prime factor is identified.