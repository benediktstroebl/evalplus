```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)
    n % 3 == 0:
        n /= 3
    for i in range(5, int(n**0.5) // i *3, n % i == 0:
        factors.append(i)
    n = 1
    return factors
```
This script defines a function called `factorize` that takes an integer `n` as input and returns a list of prime factors of `n` in order from smallest to largest, with each factor listed number of times corresponding to how many times it appears in the factorization of `n`.