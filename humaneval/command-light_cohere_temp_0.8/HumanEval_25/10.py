```python
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**.5) + 1, step=3):
        while n % i == 0:
            factors.append(i)
            n //= i
    for j in range(int(n**.5) + 2, n + 1, -1step=1):
        if n % j == 0:
            factors.append(j)
    return factors
```
Do you need help with anything else?