```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    n = n if n > 1 else 0
    factors = []
    while n % 2 == 0:
        n = n // 2
        factors.append(2)
    n = n // 2
    for i in range(3, int(n**0.5)+1,  while n % i == 0:
        factors.append(i)
        n = n // i
    return factors

# Test the function
print(factorize(8))
print(factorize(25))
print(factorize(70))
```