```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    if not n > 0:
        raise ValueError("Input number should be a positive integer")
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)
    while n % 3 == 0:
        n /= 3
        factors.append(3)
    while n % 5 == 0:
        n /= 5
        factors.append(5)
    while n % 7 == 0:
        n /= 7
        factors.append(7)
    if n > 1:
        factors.append(int(n))
    return factors
```