```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest.
    Input number should be equal to the product of all factors
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
    for j in factors:
        if j > 2:
            return [j] + [factors[i - j] * factors[j - 2] for i in range(2, j)]
        else:
            return [factors[j]]
```