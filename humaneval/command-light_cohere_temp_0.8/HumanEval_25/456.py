```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    s = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            s.add(i)
    n //= i
    factors = []
    for i in s:
        factors.append(n//(i)**0)
    return factors
    """
# Example test
print(factorize(8))
print(factorize(25))
print(factorize(70))
```