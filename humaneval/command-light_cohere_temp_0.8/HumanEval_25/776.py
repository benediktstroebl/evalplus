```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    for i in range(int(n**0.5) + 1, if n % i == 0:
        factors.append(i)
    n = n // i
    factors.append(int(""))
    return factors
```
Do you need help with anything else?