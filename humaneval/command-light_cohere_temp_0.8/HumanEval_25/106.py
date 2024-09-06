```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times corresponding to how many times it appears in factorization of the number.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(125)
    [5, 5, 5, 5]
    >>> factorize(27)
    []
    """

    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    while n > 2:
        if n % 3 == 0:
            factors.append(3)
        n //= 3
        elif n % 5 == 0:
            factors.append(5)
        n //= 5
        elif n % 7 == 0:
            factors.append(7)
        n //= 7
        else:
            break
    factors.append(n)
    return factors
```
The function factorizes the given number n into a list of its prime factors, ordered from smallest to largest.