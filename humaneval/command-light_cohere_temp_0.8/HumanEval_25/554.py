```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(56)
    [2, 2, 2, 7]
    >>> factorize(121)
    [3, 3, 7, 7]
    """
    factors = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n // i
        i += 1
    for num in range(2, int(n**0.5)+1):
        while n % num == 0:
            factors.append(num)
            n // num
    return factors
```