```python
def factorize(n: int) -> List[int]:
    """Return list of prime factors of given integer in the order from smallest to largest"""
    
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    
    for i in range(len(factors), 1, -1):
        if factors[i] > 1 and factors[i] % factors[i - 1] == 0:
            factors[i] -= factors[i - 1]
    
    return factors
```