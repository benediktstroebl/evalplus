```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times which correspond to how many times it appears in factorization.
    Input number should be equal to the product of all factors"""
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)
   
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n /= i
    return factors

# Test cases
print(factorize(8))
print(factorize(25))
print(factorize(70))
```