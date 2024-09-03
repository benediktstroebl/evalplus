```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order of appearance.
    Each factor is listed number of times it appears in factorization.
    Input number should be equal to the product of all the factors.
    """
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)

    if n > 1:
        factors.append(n)

    return factors
```