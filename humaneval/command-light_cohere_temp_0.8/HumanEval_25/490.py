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
    if n > 2:
        factors.append(n)
    return factors
``` 
This function determines the list of prime factors of the given integer n in descending order, then returns a list of those prime factors.