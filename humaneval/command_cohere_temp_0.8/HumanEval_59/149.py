```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return max(factors)
```

This approach first divides the number by 2 until it becomes odd. Then, it iterates through odd numbers from 3 to `n**0.5` and repeatedly divides `n` by each prime factor it finds. Finally, if `n` is larger than 2, it remains as the last prime factor. This solution is efficient in terms of time and space complexity, O(sqrt(n)) and O(n), respectively.