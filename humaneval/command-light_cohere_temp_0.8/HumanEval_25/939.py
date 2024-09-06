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
    >>> factorize(1000)
    [2, 2, 5, 5, 7, 11, 13, 17, 19]
    """
    if n <= 1:
        return []
    elif n % 2 == 0:
        return [n // 2] + factorize(n // 2)
    else:
        factors = []
        for i in range(3, int(n ** 0.5) + 1, while n % i == 0:
            factors.append(i)
            factors.append(n)
            while i + 1 >= n // i
        return factors
```