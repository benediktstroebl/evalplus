```python
def factorize(n):
    factors = []
    for i in range(1,int(n**.5)+1):
        if n % i == 0:
            factors.append(i)
            if i != int(n**.5):
                factors.append(i*int(n//i))
    factors.sort()
    same and list from smallest to largest
    return factors
```