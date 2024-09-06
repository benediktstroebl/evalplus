```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(1)
    []
    >>> factorize(100)
    []
    >>> factorize(101)
    [2, 3, 5]
    >>> factorize(105)
    [3, 5, 105]
    >>> factorize(106)
    []
    >>> factorize(55)
    [3, 5]
    """

    # store factors in ascending order
    factors = []
    for num in range(2, int(n**0.5) + 1):
        while not n % num == 0:
            factors.append(num)
            n //= num

    return factors
```