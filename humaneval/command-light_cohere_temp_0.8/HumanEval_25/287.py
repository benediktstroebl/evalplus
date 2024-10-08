```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(100)
    [2, 2, 5, 5, 7, 11]
    >>> factorize(333)
    Error: cannot calculate the number of prime factors
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
        for i in range(3, int(n**0.5) + 1, while n % i == 0:
            factors.append(i)
            n //= i
        return factors
```