```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(11)
    []
    >>> factorize(1)
    []
    >>> factorize(36)
    [2, 3, 6]
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    for j in range(int(n**0.5) + 1, while n % j == 0 and j != i:
        factors.append(j)
    n = n // j
    factors.sort()
    final_order of factors
    return factors
```