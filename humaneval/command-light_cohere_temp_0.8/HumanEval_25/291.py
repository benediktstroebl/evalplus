```python
from typing import List
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1, :
        while n % i == 0:
            factors.append(i)
            n = n // i
    for num in range(5, int(n ** 0) + 2, 6):
        if n % num == 0:
            factors.append(num)
    return factors
```