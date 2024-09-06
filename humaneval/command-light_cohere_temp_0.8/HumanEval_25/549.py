```python
def factorize(n):
    factors = []
    
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    for i in range(3, int(n ** 0.5) + 1, step=2):
        while n % i == 0:
            factors.append(i)
            n = n // i
        
    factors.append(int(n))
    return factors

# Uncommented test cases
# assert factorize(8) == [2, 2, 2]
# assert factorize(25) == [5, 5]
# assert factorize(70) == [2, 5, 7]
```