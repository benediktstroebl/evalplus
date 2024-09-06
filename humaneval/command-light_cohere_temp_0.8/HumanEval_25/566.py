```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times which corresponds to how many times the factor appears in factorization of the number.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    for i in range(1, int(n**0.5)+1):
        while not n % i == 0:
        factors.append(i)
        n //= i
    return factors
```