```python
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(1)
    []
    >>> factorize(14)
    [2, 7]
    >>> factorize(100)
    [2, 2, 5, 5, 10]
    """
    if n <= 1:
        return []
    elif n <= 3:
        return [n]
    else:
        factors = []
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        while n % 7 == 0:
            factors.append(7)
        while n % 12 == 0:
            factors.append(12)
        while n % 25 == 0:
            factors.append(25)
        while n % 8 == 0:
            factors.append(8)
        while n % 3 == 0:
            factors.append(3)
        return factors
```