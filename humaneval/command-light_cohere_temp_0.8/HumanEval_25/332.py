```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times corresponding to how many times it appears in factorization
    Input number should be equal to the product of all the factors.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    if n <= 1:
        return []
    if n <= 3:
        return [1]
    factors = [1]
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n = n // i
    for i in factors:
        if i != 1:
            return factors + [i]
    return factors
```