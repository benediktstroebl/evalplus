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
    >>> factorize(91)
    [7, 3, 3]
    >>> factorize(53)
    [3, 3, 7]
    >>> factorize(123)
    [2, 3, 3, 2]
    """
    factors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0: factors.append(i)
        n //=i
    while n % i == 0: factors.append(i)
    n //=i
    return factors
```
The function, `factorize()`, takes an integer `n` as input and returns a list of prime factors of `n` in order from smallest to largest. Each of the factors are listed number of times corresponding to how many times it appears in factorization. The function uses trial and loop to find the prime factors of the number.