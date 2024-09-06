```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(500)
    [2, 2, 5, 5, 7, 11]
    >>> factorize(0)
    []
    >>> factorize(-2)
    []
    """
    s=set(range(2,int(n**0.5)+1))
    s=list(s)
    return [x for x in s if x<=n and x]
```