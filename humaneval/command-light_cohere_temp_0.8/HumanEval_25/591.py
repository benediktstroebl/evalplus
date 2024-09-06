```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times which corresponds to the number of times it appears in factorization of the number
    Input number should be a product of prime factors.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(100)
    [2, 2, 5, 5, 7]
    >>> factorize(250)
    [2, 2, 5, 5, 5, 7]
    """
    #List all the factors
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
   
    # Sort the factors in descending order.
    factors.sort(key=lambda(factors[i], factors[i-1]) for i in range(1, len(factors))-1)
    return factors
```