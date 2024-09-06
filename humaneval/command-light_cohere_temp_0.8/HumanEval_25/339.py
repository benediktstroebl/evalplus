```python
def factorize(n: int) -> List[int]:
    factors = []
    for i in range(2,int(n**.5)+1):
        is_divisible = n%i == 0
        if is_divisible:
            factors.append(i)
            if i == int(n**.5):
                break
    return factors
```