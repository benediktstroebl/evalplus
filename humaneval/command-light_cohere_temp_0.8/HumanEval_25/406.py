```python
from typing import List
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        i += 2
    for num in factors:
        if num > 1:
            factors.append(factorize(num))
    return factors
```