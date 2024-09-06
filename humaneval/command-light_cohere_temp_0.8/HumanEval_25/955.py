```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(100)
    [2, 5, 5, 7, 11]
    >>> factorize(55)
    [5, 11]
    >>> factorize(111)
    [3, 7, 11]
    """
    if n <= 1:
        return []

    # you can uncomment this line to print the candidate factors
    # print(f"candidates: {list(range(2, int(n**0.5))})")

    # list of factors is already sorted in decreasing order, so we will pick first one
    factors = [2, 3, 5]
    while n % factors[0] == 0:
        n //= factors[0]
        factors.append(factors[0])

    factors.extend(factors[1:]

    return factors

```