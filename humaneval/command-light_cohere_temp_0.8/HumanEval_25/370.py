```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times which corresponds to how many times it appears in factorization
    Input number should be equal to the product of all the factors.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(120)
    [2, 2, 2, 3, 5, 5, 7]
    >>> factorize(900)
    [3, 5, 3, 3, 6, 2, 2, 2, 2]
    """
    # stores the multiplications factors
    factors = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n = n / i
    for j in factors:
        factors.extend(factors[j] * j, factors[j] = j
    return factors
```