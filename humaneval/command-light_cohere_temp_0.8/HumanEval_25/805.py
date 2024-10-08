```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)
    n % 3 == 0:
        n /= 3
        factors.append(3)
    n % 5 == 0:
        n /= 5
        factors.append(5)
    n % 7 == 0:
        n /= 7
        factors.append(7)
    return factors
```
The function factors out the prime factors of the given number n, ensuring the factors are in order from the smallest prime factor to the largest.

Do you need help with anything else?