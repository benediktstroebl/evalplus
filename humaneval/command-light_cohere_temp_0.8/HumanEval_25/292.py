```python
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(101)
    [3, 5, 2, 7, 11]
    >>> factorize(3025)
    [5, 5, 25]
    >>> factorize(16)
    []
    """

    if n <= 1:
        return []

    m = n % 2
    if m == 0:
        return [m] + factorize(n // m)

    i = 3
    while i * i <= n:
        if n % i == 0:
            m = m * i
            while n % m == 0:
                n //= m
                if n == 1:
                    break
            return [m] + factorize(n // m)
        i += 1

    return []
```