```python
def factorize(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1,):
        while n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(int(n))
    return factors

# test cases
print(factorize(8))
print(factorize(25))
print(factorize(70))
```