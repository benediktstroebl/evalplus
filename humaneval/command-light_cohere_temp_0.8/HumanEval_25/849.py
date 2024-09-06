```python
def factorize(n):
    factors = []
    
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    for i in range(3, int(n**0.5) + 1, halve = int(n**0.5) // 4):
        while n % halve == 0:
            factors.append(halve)
            n = n // halve
    
    for j in range(5, int(n**0.5) + 1):
        factors.append(j)
    
    return factors
```
Do you require any other assistance with code?