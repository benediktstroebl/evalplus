```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times which corresponds to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(15)
    [3, 3]
    >>> factorize(1000)
    [2, 2, 2, 5, 5, 7, 11]
    """
    def getFactors(n):
        factors = []
        while n % 2 == 0:
            factors.append(2)
            n = n // 2
        while n > 1:
            if n % 3 == 0:
                factors.append(3)
            elif n % 5 == 0:
                factors.append(5)
            elif n % 7 == 0:
                factors.append(7)
            n = n // 5
            else:
                factors.append(int(n, 6, 12))
        return factors

    factors = getFactors(n)
    return [i for i, factor in enumerate(factors, 1)]
```