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

This approach first exhausts the even factors and then moves through the odd factors iterating from 3 up to `n**0.5`. The code is streamlined to handle the prime factorization of any number and extract the largest prime factor.

This solution surpasses the given tests:
```python
>>> largest_prime_factor(13195)
29
>>> largest_prime_factor(2048)
2
```