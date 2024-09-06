```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(105)
    [5, 5, 7, 3]
    >>> factorize(0)
    []
    >>> factorize(-1)
    []
    >>> factorize(10)
    []
    """
    
    if n <= 1:
        return []
    
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    while n % 3 == 0 and n > 2:
        factors.append(3)
        n = n // 3
    
    for i in range(4, int(n ** 0.5) + 1, i += 4):
        factors.append(i)
        n = n // i
    
    if len(factors) > 1:
        factors.append(int(n))
    
    return factors
```