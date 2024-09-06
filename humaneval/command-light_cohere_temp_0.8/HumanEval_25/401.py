```python
from typing import List
def factorize(n: int) -> List[int]:
    """Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times corresponding to how many times it appears in factorization of the number.
    Input number should be equal to the product of all factors.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    while n > 1:
        if n % 2 == 0:
            factors.append(2)
        n = n // 2
        else:
            i = 3
            while i <= int(n**0.5/2):
                factors.append(i)
                n = n // i
            i += 2
    return factors
```