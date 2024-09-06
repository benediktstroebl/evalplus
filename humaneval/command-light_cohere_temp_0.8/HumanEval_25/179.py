```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times which corresponds to the power it has in factorization of n.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(50)
    [2, 2, 5, 5]
    >>> factorize(100)
    [2, 2, 2, 5, 5, 5]
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    while n > 1:
        if n % 3 == 0:
            n //= 3
        elif n % 5 == 0:
            n //= 5
        elif n % 7 == 0:
            n //= 7
        else:
            factors.append(n)
        n //= n //2 

    # return list of prime factors
    return factors
```