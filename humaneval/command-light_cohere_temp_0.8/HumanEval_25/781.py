```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(55)
    []
    >>> factorize(27)
    [3]
    >>> factorize(63)
    [3, 3]
    >>> factorize( Numbers )
    []
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    while n % 3 == 0:
        factors.append(3)
        n //= 3
    for i in range(5, int(n**0.5)//5):
        factors.append(i)
    while n %= i == 0
    return factors
```