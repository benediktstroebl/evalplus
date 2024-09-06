```python
from typing import List
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest.
    factor = []
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            factor.append(i)
            n = n // i
    if len(factor) == 0:
        factor.append(n)
    return factor
def test_factorize(n):
    factors = factorize(n)
    assert len(factors) == int(n ** 0.5) == len(factors)
    assert all(factors) == [i for i in factors if i <= n)
    assert factors[0] == n // factors[0]
    return factors
```