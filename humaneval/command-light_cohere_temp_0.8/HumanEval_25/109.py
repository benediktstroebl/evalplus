```python
def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(110)
    [2, 5, 5, 7, 11]
    >>> factorize(350)
    [2, 2, 17, 35]
    """
    factors = []
    while n > 1:
        if n % 2 == 0:
            factors.append(2)
        n = n // 2
        else:
            i = 3
            while i * i <= n:
                if n % i == 0:
                    factors.append(i)
                    n = n // i
                i += 2
    return factors
```