```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times, which corresponds to how many it appears in factorization
    Input number should be equal to the product of all its factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(1000)
    []
    >>> factorize(27)
    []
    """
    s = set(divmod(n, n))
    l = []
    while s:
        x = s.pop()
        n //
        l.append(x factor(x))
        s.clear()
    #.pop()
    total,
    for i in range(0, len(l)):
    l[i] *= l[i]
    return l
```