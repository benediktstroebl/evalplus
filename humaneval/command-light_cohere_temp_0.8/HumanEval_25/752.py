```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
        n = n // i
        i += 2
    for num in range(3, int(n ** 0.5) + 1,  while n % num == 0:
            factors.append(num)
        n = n // num
    for num in factors:
        if num <= 1:
            factors.remove(num)
        return factors
```