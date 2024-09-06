```python
def factorize(n: int) -> List[int]:
    factors = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0: factors.append(i)
        n //= i
    while len(factors) < len(set(factors)): factors.append(factors[-1]) * factors[i]
    return factors
```