```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    All prime factors should be listed number of times corresponding to how many times they appear in factorization
    of n
    """
    factors = []
    for i in range(1, int(n ** 0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    factors.append(n)  # Add last factor
    return factors

# Test the function
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```