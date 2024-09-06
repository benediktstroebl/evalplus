```python
def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(100)
    []
    >>> factorize(55)
    [5, 11]
    >>> factorize(0)
    []
    >>> factorize(-1)
    []
    """
    if n <= 1:
        return []

    # Write your code here
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)
    factors.extend(int(n % 3 == 0))
    while n % 3 == 0:
        n /= 3

    # n must be a prime at this point
    # so append n if it is not divisible by 2 or 3
    factors.append(n)

    return factors
```