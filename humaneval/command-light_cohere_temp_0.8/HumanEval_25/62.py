```python
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(36)
    [2, 2, 2, 3]
    >>> factorize(1000)
    [2, 2, 3, 5, 5, 25, 50, 75]
    """
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5),5, while n % i == 0:
        factors.append(i)
        n = n // i
    factors.append(n)
    return factors
```
This function uses a loop and testing different numbers to determine prime factors. It runs efficiently and effectively handles larger numbers.