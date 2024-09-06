```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times, corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(54)
    [2, 3, 3, 7]
    >>> factorize(100)
    [2, 2, 5, 5, 10, 25]
    """
    s = set(range(2, int(n**0.5)+1))
    possible_factors = []
    while s:
        i = len(s) - 1
        d = 2
        while d <= i and d * d <= n:
            s.remove(d)
            d += 1
        possible_factors.append(d)
    
    return possible_factors
```