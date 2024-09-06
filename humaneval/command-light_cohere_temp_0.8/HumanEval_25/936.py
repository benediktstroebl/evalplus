```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be the number itself number of times, and be listed in the order of increasing power of the number.
    >>> factorize(8)
    [2, 2]
    >>> factorize(25)
    [5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(55)
    [5, 11]
    >>> factorize( Number(){}) 
    []
    """
    if n <= 1:
        return []

    d = n // 2
    s = []
    while d*d > n:
        s.append(d)
        d = d // 2

    for m in range(2, int(n**0.5)+1):
        while n % m == 0:
        s.append(m)
        n = n // m

    if s == []:
        return [n]

    return s
```