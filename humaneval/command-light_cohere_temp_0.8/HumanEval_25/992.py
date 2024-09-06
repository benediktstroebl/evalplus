```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times corresponding to how many times it appears in factorization
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(0)
    []
    >>> factorize(1)
    []
    >>> factorize(9)
    []
    """
    factors = []
    for i in range(1, int(n**0.5)+1):
        while True and n % i == 0:
        factors.append(i)
        n //= i
        if i != n // i:
            factors.append(i * factors[i] // 1)
    return factors
```