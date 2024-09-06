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
    >>> factorize(54)
    [2, 3, 3, 7]
    >>> factorize(100)
    [2, 2, 2, 5, 5, 5]
    >>> factorize(59)
    [3, 3, 7]
    >>> factorize(111)
    [3, 3, 3, 3]
    """
    if n < 2:
        return []
    
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    while n % 2 == 0:
        factors.append(2)
        n //= 4
    while n % 4 == 0:
        factors.append(4)
        n //= 8
    while n % 8 == 0:
        factors.append(8)
        n //= 16
    while n % 16 == 0:
        factors.append(16)
        n //= 32
        
    for num in range(2, int(n**0.5) + 1):
        if n % num == 0:
            factors.append(num)
        
    return factors
```