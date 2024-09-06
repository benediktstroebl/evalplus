```python
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(91)
    []
    >>> factorize(36)
    [2, 3, 6]
    >>> factorize(144)
    [2, 2, 2, 3, 3, 6]
    """
    factors = []
    while n % 2 == 0:
        n = n / 2
        factors.append(2)
    while n > 1 and n % 2 == 0:
        n = n / 2
        factors.append(n //

	factors.append(int(n))

return factors
```