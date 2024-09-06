```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times which corresponds to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(81)
    [3, 3, 7]
    >>> factorize(10**100)
    [2, 5, 5, 2**100]
    """
    factors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0: factors.append(i)
    if n != n // i: factors.append(i*i)
    return factors
```
This function will provide a list of prime factors of a given number, ordered from the smallest to the largest. It will also list each factor in the factorization corresponding to how many times it appears.