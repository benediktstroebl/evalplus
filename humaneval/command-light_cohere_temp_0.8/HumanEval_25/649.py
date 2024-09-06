```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed in the order of how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(300)
    [2, 2, 3, 5, 7, 11]
    >>> factorize(1025)
    [5, 5, 25]
    >>> factorize(134629)
    [2, 2, 46, 293]
    """
    if n <= 1:
        return []
    if n % 2 == 0:
        return [n // 2] + factorize(n // 2)
    factors = []
    while n % 2 == 0:
        factors.append(n // 2)
        n = n // 2
    factors += factorize(n)
    return factors
```  The function uses the `factorize` function which takes an integer as a parameter and returns a list of prime factors of that number in descending order.  The function then uses a simple algorithm to find the prime factors of a given number.