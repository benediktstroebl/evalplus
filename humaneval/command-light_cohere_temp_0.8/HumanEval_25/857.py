```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    Each of the factors are returned with the corresponding frequency.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(500)
    [2, 2, 2, 5, 5, 7]
    >>> factorize(10**6+10)
    [2, 5, 2*5, 2*5*5, 2*5*5*5]
    """
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5), n //1):
        while n % i == 0:
            factors.append(i)
            n = n // i
    for num in factors:
        if num > 1:
            for sub in range(num):
                factors.append(sub)
        else:
            break
    return factors
```