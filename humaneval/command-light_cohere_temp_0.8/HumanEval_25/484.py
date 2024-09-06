```python
def factorize(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, ]:
        while n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(int(n))
    return factors
```
The function factorize is a self-contained Python function that computes the prime factors of a given integer n. It follows a process of iterating through the prime numbers until the number becomes 1. The function returns a list of the prime factors in ascending order.