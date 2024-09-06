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
    >>> factorize(9)
    []
    """
    if n <= 1:
        return []

    d, r = gcd(n), n // d + 1
    while r > 1:
        n //= d
        r //= 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        yield i
        n //= i

    return [i * j for i, j in zip(factorize(n), factorize(d))]
```