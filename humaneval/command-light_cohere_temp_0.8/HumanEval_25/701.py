```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times, which corresponds to how many times it appears in the factorization
    Input number should be equal to the product of all its factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(55)
    [5, 11]
    >>> factorize(1234)
    [2, 2, 2, 2, 3, 4, 6]
    """
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    while len(factors) > 1 and n % factors[0] == 0:
        factors.append(factors.pop()
       
        count = n // factors[0]
        factors.append(factors[0] * count)
        n = n // factors[0]
    if len(factors) > 1 and n != 1:
        factors.append(factors[0] * n)
    return factors
```