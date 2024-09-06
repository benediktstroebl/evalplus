```python
def factorize(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1,):
        while n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(n)
    return factors
```
The function factorize calculates the list of prime factors of the given number n and returns the list in order from the smallest factor to the largest one. 

This function works efficiently, and it doesn't rely on external libraries.