```python
from typing import List
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest.
    if not n:
        return []
    factors = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
        factors.append(i)
        n = n // i
    factors.append(n)
    return factors
def test_factorize():
    assert factorize(8) == [2, 2, 2]
    assert factorize(25) == [5, 5]
    assert factorize(70) == [2, 5, 7]
```