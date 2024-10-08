```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    for i in range(int(n**0.5) + 2, while n % i == 0 and i > 2:
        factors.append(i)
    n = n // i
    return factors
```