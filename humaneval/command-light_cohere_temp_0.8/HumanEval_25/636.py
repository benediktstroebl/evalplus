```python
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1,):
        while n % i == 0:
            factors.append(i)
            n //= i
    factors.append(n)
    return factors
```
The function uses a while loop and basic factors to factorize an integer n.