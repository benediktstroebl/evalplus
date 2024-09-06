```python
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(50)
    [] # Not a prime number
    >>> factorize(13)
    [13] # Only one factor
    """
    if n <= 1:
        return []
    elif n <= 3:
        return [n]
    elif n % 2 == 0 or n % 3 == 0:
        return [n] + factorize(n // 3)
    else:
        factors = []
        for i in range(5, int(n ** .5) + 1, 6):
            if n % i == 0:
                factors.append(i)
                if len(factors) == 1:
                    break
        return factors
```