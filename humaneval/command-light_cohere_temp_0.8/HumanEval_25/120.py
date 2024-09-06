```python
def factorize(n):
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
                i += 2
    return factors
```