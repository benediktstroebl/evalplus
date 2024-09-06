```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times corresponding to how many times it appears in factorization of the number
    Input number should be equal to the product of all its factors.
    >>> [2, 2, 2]
    >>> factorize(8)
    [2, 2, 2]
    >>> [2] * [5, 5] = 25
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    while n % 4 == 0:
        factors.append(2)
        n //= 4
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(int(i))
        n //= i
    for j in factors:
        factors.append(j * int(n//j))
    return factors
```