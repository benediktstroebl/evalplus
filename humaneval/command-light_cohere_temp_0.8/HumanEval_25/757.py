```python
from typing import List
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest.
    If factorize(8)
    >[:] [2, 2, 2]
    >[:] factorize(25)
    >[:] [5, 5]
    >[:] factorize(70)
    """
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            yield i
            while n % i == 0:
                n //= i
    return 
```