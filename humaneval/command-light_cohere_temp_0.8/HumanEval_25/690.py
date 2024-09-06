```python
def factorize(n):
    factors = []
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
        factors.append(i)
        n //= i
    else: continue
    return factors

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```