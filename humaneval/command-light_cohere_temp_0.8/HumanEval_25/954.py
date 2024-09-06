```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times, which corresponds to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(50)
    [2, 2, 5, 5]
    >>> factorize(100)
    [2, 2, 2, 5, 5, 5]
    """
    if n <= 1:
        return []
    elif n % 2 == 0:
        return [n // 2] + factorize(n // 2)
    else:
        factors = []
        while n % 2 == 0:
            factors.append(n / 2)
            n = n // 2
        else:
            for i in range(3, int(n ** .5) + 1, 2):
                if n % i == 0:
                    factors.append(i)
                    n = n / i
        return factors
```