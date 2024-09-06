```python
def factorize(n):
    factors = []
    
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    while n > 1:
        if n % 3 == 0:
            factors.append(3)
            n //= 3
        elif n % 5 == 0:
            factors.append(5)
            n //= 5
        elif n % 7 == 0:
            factors.append(7)
            n //= 7
        else:
            factors.append(int(n % d for d in range(1, 10)))
            n //= int(n % d)

    return factors
```