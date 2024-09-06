```python
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(55)
    [5, 11]
    >>> factorize(7*11*7)
    [7, 11, 7]
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) // n % 2 == 0:
        factors.append(int(f)**i)
        n = n // int(f)**i
    for i in range(int(n**0.5) + 1):
        factors.append(int(n)**i)
    return factors
```