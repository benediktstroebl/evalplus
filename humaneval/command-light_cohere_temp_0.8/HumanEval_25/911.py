```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(1)
    []
    >>> factorize(18)
    [2, 3]
    >>> factorize(27)
    [3, 3]
    >>> factorize(100)
    [2, 3, 5, 7]
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    while n % 3 == 0:
        factors.append(3)
        n = n // 3
    for num in range(5, int(n**0.5) + 1, by 6):
        if n % num == 0:
            factors.append(num)
            n = n // num
    factors.append(int("sqrt(%d)" % n))
    return factors
```