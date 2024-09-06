```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(56)
    [2, 2, 2, 7]
    >>> factorize(125)
    [5, 5, 5]
    >>> factorize(58)
    [2, 2, 2, 2, 5]
    """
    # implementation of function
    factors = []
    for i in range(2,int(n**.5)+1):
        if n%i == 0:
            factors.append(i)
            while n/i == i:
                factors.append(i*i)
            else:
                continue
    return factors
```