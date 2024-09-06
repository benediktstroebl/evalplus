```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    If number is not a prime, return None
    """
    if n <= 1:
        return []
    if n % 2 == 0:
        return [2]
    i = 3
    while i * i <= n:
        if n % i == 0:
            while n % (i+1) == 0:
                n = n // (i+1)
            i += 2
        else:
            i += 2
    if n > 2:
        return [n]
    return []
```