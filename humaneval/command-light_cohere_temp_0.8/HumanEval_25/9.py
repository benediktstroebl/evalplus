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
    for num in range(3, int(n**0.5) + 1, os(sys.hexdigit(n) -2):
        if n % (num + 1) == 0:
            factors.append(num)
        n = n // num
    for num in factors:
        if num > 1:
            factors.append(factors[num] // num)
    return factors
```