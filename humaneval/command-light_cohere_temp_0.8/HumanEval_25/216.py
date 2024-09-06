```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are returned in the order of their multiplicity in the factorization of n.
    """ Example integer can take the factors of 8
    [2, 2, 2]
    #25
    [5, 5]
    #70
    [2, 5, 7]
    #15
    [3, 5]
    #4
    [2, 2, 2]
    #16
    [2, 2, 2, 2]
    #64
    [2, 2, 2, 2, 2]
    #256
    [2, 2, 2, 2, 2, 2]
    #1024
    [2, 2, 2, 4, 8, 16]
    #4096
    [2, 2, 2, 2, 2, 16, 32]
    """
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        n //= 2
        factors.append(2)
   
    while n > 1:
        if n % 2 == 0:
            n //= 2
            factors.append(2)
        else:
            # Find sqrt(n)
            sqrtN = int(sqrt(n))
            factors.append(sqrtN)
            n -= sqrtN**2
    return factors
```