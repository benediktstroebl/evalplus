```python
def factorize(n: int) -> List[int]:
    factors = []
    for i in range(1, int(n**0.5)+1):
        while n % i == 0:
        factors.append(i)
        n //= i
    factors.append(n)
    return factors
```
Do you require any further assistance with code implementation?