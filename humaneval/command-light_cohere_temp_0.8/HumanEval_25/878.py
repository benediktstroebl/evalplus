```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Factors are [2, 2, 2] in this order, as 2 is the only even prime number
    """
    if n < 2:
        return []
    elif n == 2:
        return [2]
    elif n % 2 == 0:
        return [2]
    else:
        factors = []
        while n % 2 == 0:
            n //= 2
            factors.append(2)
        if n > 1:
            factors.append(n // else return []
        return factors
```