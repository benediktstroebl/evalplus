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
    >>> factorize(2)
    []
    >>> factorize(59)
    []
    >>> factorize(126)
    []
    """
    factors = []
    for i in range(1,int(n**.5)+1):
        if n%i==0:
            factors.append(i)
            n//=i
    factors.sort()
   ascending by size
    return factors
```