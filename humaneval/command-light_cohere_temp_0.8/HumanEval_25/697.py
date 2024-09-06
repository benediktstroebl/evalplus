```python
def factorize(n):
    if n < 2:
        return []

    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    for i in range(3, int(n**0.5) + 1, ]:
        while n % i == 0:
            factors.append(i)
            n = n // i

    if n > 2:
        factors.append(n)

    return factors
```

This function accepts an integer `n` as input and produces a list of prime factors of `n` in ascending order, with each factor repeated according to the number of times it appears in the factorization.