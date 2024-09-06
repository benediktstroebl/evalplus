```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n = n // i
        i += 2
    for j in range(3, int(n ** 0.5) + 1,  while j <= n and n % j == 0:
            factors.append(j)
        n = n // j
    return factors
```