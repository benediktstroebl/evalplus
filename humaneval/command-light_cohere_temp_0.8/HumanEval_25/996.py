```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(100)
    [2, 2, 5, 5, 7, 11]
    >>> factorize(55)
    [5, 11]
    >>> factorize(333)
    []
    """
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)
    while n > 1 and n % 3 == 0:
        n /= 3
    while n > 1:
        factors.append(int(n))
        n /= int(n**0.25)
    factored so far
    # n will always be the last element in the list
    return factors
```