```python
def factorize(n: int) -> List[int]:
    factors = []
    while n > 1:
        if n % 2 == 0:
            factors.append(2)
        n //= 2
        else:
            i = 3
            while i * i <= n:
                if n % i == 0:
                    factors.append(i)
                    n //= i
            else:
                    break
        else:
            break
    return factors
```