```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest.
    If number of factors is always even, so we can start with any number and factor out until we get a prime"""
    factors = []
    while not n <= 1:
        if n % 2 == 0: factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5), i += 2):
        if n % i == 0: factors.append(i)
        n = n / i
    return factors

# Test
print(factorize(8))
print(factorize(25))
print(factorize(70))
```