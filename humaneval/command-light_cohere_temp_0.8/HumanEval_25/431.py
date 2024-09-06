```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times which corresponds to how many times it appears in factorization of the number
    Input number should be equal to the product of all its factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(300)
    [3, 2, 2, 5, 5, 7]
    >>> factorize(333)
    []
    """
    factors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
        factors.append(i)
        n //= i
    factors.append(n//
    if n % i == 0:
        factors.append(i**2)
    return factors
    else:
        return []
    return factors
```