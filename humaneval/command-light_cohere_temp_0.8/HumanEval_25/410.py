```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be the same number of times in factorization corresponding to its position.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(81)
    [3, 3, 7]
    >>> factorize(55)
    [5, 11]
    >>> factorize(133)
    [3, 3, 13]
    >>> factorize(999)
    [3, 7, 9, 3]
    """
    # Generate factors
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    while n % 3 == 0:
        factors.append(3)
        n //= 3
    while n % 5 == 0:
        factors.append(5)
        n //= 5
    while n % 7 == 0:
        factors.append(7)
        n //= 7
    for num in factors:
        while n % num == 0:
            n //= num
            break
    return factors
```