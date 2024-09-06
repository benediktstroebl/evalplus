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
    >>> factorize(77)
    [7, 7]
    >>> factorize(100)
    [2, 2, 5, 5, 7, 11]
    """
    s = set(range(2,int(n**0.5)+1))
    if n in s:
        return [n] + [x for x in s if x*x <= n]
    else:
        return [n] + [x for x in s if x**2 + x == n]
```