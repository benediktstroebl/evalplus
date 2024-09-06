```python
def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(50)
    [2, 2, 5]
    >>> factorize(100)
    [2, 2, 2, 5, 5]
    """
    if n <= 1:
        return []
    if n % 2 == 0:
        return [2]
    factors = []
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        if n % i == 0:
            break
    return factors
```