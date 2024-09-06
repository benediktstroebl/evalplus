```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(49)
    [7]
    >>> factorize(97)
    [3, 3, 7]
    >>> factorize(56)
    []
    """
    s= []
    while n%2==0:
        s.append(n// 2)
        n=n//2
    for i in range(3, int(n**0.5) + 1, while n%=(i*i) == 0:
        s.append(n// i)
        n = n//i
    if n>2:
        s.append(n)
    return s
```