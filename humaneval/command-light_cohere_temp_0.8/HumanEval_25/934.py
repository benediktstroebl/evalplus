```python
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
    if n > 2 and n % 2 == 0:
        factors.append(2)
    return factors
```
This function takes an integer n as input and returns a list of prime factors of n in descending order, as per the given prompt.