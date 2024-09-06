```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest.
    For big integers, prime factorization may not terminate.
    """
    example:
    >>> factorize(128)
    [2, 2, 2, 2, 4, 2, 4, 4, 4]
    """
    if n < 2:
        return []
    
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    while n % 3 == 0:
        factors.append(3)
        n = n // 3
    while n % 5 == 0:
        factors.append(5)
        n = n // 5
    while n % 7 == 0:
        factors.append(7)
        n = n // 7
        
    for num in factors:
        if num > 2:
            break  # To prevent adding the same factor multiple times
    
    return factors
```