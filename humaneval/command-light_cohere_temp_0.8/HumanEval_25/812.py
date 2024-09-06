```python
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(111)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: 'int' object is integer-valued, cannot divide by zero
    """
    if n == 0:
        raise ZeroDivisionError("'int' object is integer-valued, cannot divide by zero")

    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1,):
        while n % i == 0:
            factors.append(i)
            n = n // i
    for j in factors:
        factors.append(factors.count(j)
        if j != 1:
            factors.append(factors.count(factors.count(j))
    if len(factors) == 1:
                break
    return factors
```