```python
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(77)
    [7, 7]
    >>> factorize(100)
    [2, 2, 2, 5, 5, 7, 11]
    >>> factorize(101)
    [3, 5, 101]
    """
    factors = []
    while n > 1:
        d = divmod(n, 2)
        if d[1] == 0:
            factors.append(d[1])
        n = n // 2
    for i in range(3, int(n**0.5) + 1,:
        if n % i == 0:
            factors.append(i)
        n = n // i
    return factors
```