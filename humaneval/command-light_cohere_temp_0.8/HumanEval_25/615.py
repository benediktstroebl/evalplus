```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(100)
    []
    >>> factorize(3)
    []
    """
    if n <= 1:
        return []

    d = 0
    for i in range(2, int(n**0.5) + 1):
        while d < n:
            if n % i == 0:
                d += 1
                while n % i == 0:
                    n //=i

    factors = [d]
    for i in range(2, int(n**0.5) + 1):
        while d < n:
        while n % i == 0:
            n //=i
            d += 1
        factors.append(d)

    return factors
```
This Python function, `factorize()`, takes an integer `n` as input and returns a list of its prime factors in order from smallest to largest. It iterates through loop to find the smallest prime factor and keeps track of how many times it appears in factorization.