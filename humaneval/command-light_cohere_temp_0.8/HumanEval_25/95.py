```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(73)
    [3, 2, 7]
    >>> factorize(50)
    [2, 2, 5]
    >>> factorize(125)
    [5, 5, 25]
    """
    if n <= 1:
        return []
    if n <= 3:
        return [n]
    factors = []
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            factors.append(i)
            if len(factors) == i:
                break
        else:
            for j in factors:
                if n % j == 0:
                    break
    return factors
```