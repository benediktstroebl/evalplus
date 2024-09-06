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
    >>> factorize(123)
    [2, 3, 5, 7]
    >>> factorize(boosted)
    [2, 2, 3, 5, 7, 11]
    """
    if n < 2:
        return []

    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i

    for i in range(int(n**0.5) + 2, while n % i == 0:
        factors.append(i)

    factors.append(1)  # If any prime factors greater than the square of the number remain

    return factors
```