```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(55)
    [5, 11]
    >>> factorize(1000)
    []
    """
    s = set(1) 
    while n > 1: 
        t = n // n 
        if t > 1 and t not in s: 
            s.add(t) 
        n = n // t 
    factors = [t for t in s if t <= n]
    return factors
```