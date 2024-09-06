```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(2)
    []
    >>> factorize(10)
    [2, 5]
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    while n % 4 == 0:
        factors.append(4)
        n //= 4
    while n % 8 == 0:
        factors.append(8)
        n //= 8
    for x in range(10, n //2 + 1, -1):
        if x * x <= n and x is not divisible(n):
            factors.append(x)
    return factors
```
This script defines a function called `factorize` which takes an integer n as input and returns a list of prime factors of n, ordered from smallest to largest. The function uses a trial and error approach to find prime factors, checking divisibility by square and odd factors until the number cannot be factored any further.