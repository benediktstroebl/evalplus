```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(15)
    []
    >>> factorize(11)
    []
    """

    factor_set = set()
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factor_set.add(i)
            n //= i

    if len(factor_set) == 1:
        return [factor_set.pop()]
    if len(factor_set) > 1:
        return factor_set
    
    return []
```