```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times, which corresponds to how many times it appears in the factorization of the number
    Input number should be equal to the product of all its factors. Returns list of numbers, as the number is itself, it is considered a prime factor.
    >>> factorize(8)
    [8]
    >>> factorize(25)
    [5]
    >>> factorize(70)
    [2, 7]
    """
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(n)
    n 
    factors.append(n)
    while n > 1 and n % 2 == 0 
    factors.append(n)
    return factors
```
The function returns a list of prime factors in the order of their appearance in the factorization of the number.