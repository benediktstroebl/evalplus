```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times, corresponding to how many times they appear in the factorization of the input number.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(73)
    [] # Returns empty list for non-prime numbers
    """
    factors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
        factors.append(i)
        n //=i
    return factors
```