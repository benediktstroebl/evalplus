```python
def factorize(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1, step = 2** * i:
        while n % step == 0:
            factors.append(step)
            n = n // step
    for j in range(int(n ** 0.5) + 2, step = 2** * i + 1:
        while n % step == 0:
            factors.append(step)
            n = n // step
    return factors
```