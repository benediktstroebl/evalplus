```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(100)
    [2, 2, 5, 5, 7, 11]
    """
    s=set(range(2,int(n**0.5)+1))
    using sieve of eratostics
    # print(s)
    factors:=[i for i in s if i<=n]
    # print(factors)
    # sort the list of factors
    factors.sort()
    rema ordering, which ensures that the factors are returned in order from smallest to largest.
    return factors

```
Do you need assistance with anything else? I can provide you with further code snippets or help you solve other coding problems.