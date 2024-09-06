```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times which corresponds to how many times it appears in factorization
    Input number should be equal to the product of all its factors.
    >>> [2, 2, 2] is a prime factorization of 8
    >>> [5, 5] is a prime factorization of 25
    >>> [2, 7, 2] is a prime factorization of 70
    """
    if n <= 1:
        return []

    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    for i in factors:
        if i > 1:
            factors.append(factors[i] * i)
    return factors
```