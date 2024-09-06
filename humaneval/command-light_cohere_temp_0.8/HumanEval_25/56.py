```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(10)
    []
    >>> factorize(11)
    []
    >>> factorize(1)
    []
    """

    if n <= 1:
        return []

    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    while n % 3 == 0:
        factors.append(3)
        n = n // 3
    while n % 5 == 0:
        factors.append(5)
        n = n // 5
    while n % 7 == 0:
        factors.append(7)
        n = n // 7
    while n % 11 == 0:
        factors.append(11)
        n = n // 11
    while n % 13 == 0:
        factors.append(13)
        n = n // 13
    while n % 17 == 0:
        factors.append(17)
        n = n // 17
    while n % 19 == 0:
        factors.append(19)
        n = n // 19
    while n % 23 == 0:
        factors.append(23)
        n = n // 23
    if n <= 1:
        return []

    return factors
```