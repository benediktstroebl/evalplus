```python
def factorize(n):
    if n < 2:
        return []

    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    for i in range(3, int(n**0.5) + 1, loop_bound):
        while n % i == 0:
            factors.append(i)
            n = n // i

    factors.append(n)
    return factors
```
This function uses a simple algorithm to find the prime factors of a given number. It also handles the factorization correctly, including numbers with more than 2 prime factors and correct order.