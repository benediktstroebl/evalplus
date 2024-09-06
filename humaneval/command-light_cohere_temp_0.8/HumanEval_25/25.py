```python
def factorize(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
        i += 2
    if n > 2:
            factors.append(n)
    return factors
```
The function first handles the case where the number is even and then uses the fact that all prime factors greater than 2 are of the form 6k + 1k for some integer k. It then iterates through numbers from 3 upwards until it finds one that divides the number evenly.