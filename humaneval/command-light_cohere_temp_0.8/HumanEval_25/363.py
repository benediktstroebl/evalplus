```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be the number of times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(100)
    [2, 2, 5, 5, 7, 11]
    """
    factors = []
    while n > 1:
        if n % 2 == 0:
            factors.append(2)
        n = n // 2
        else:
            for i in range(3, int(n**0.5), i += 2):
                if n % i == 0:
                    factors.append(i)
                    n = n // i
    factors.append(n)
    return factors
```
This script defines a function factorize that calculates and returns a list of prime factors for a given integer. It iterates through loop until the n becomes 1 and checks if n is prime by testing divisibility with 2, then iterates through the list from 3 up, adding the factors to the list as we find them. The function tests tests the fact that the order of the prime factors will be in increasing order, starting from the smallest factor up to the largest factor.