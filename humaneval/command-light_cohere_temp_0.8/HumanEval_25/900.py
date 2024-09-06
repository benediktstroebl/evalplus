```python
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**.5) + 1, by=2):
        while n % i == 0:
            factors.append(i)
            n //= i
    for i in range(int(n**.5) + 2, n + 1, by=2):
        factors.append(i)
    return factors
```
Do you need assistance with anything else?