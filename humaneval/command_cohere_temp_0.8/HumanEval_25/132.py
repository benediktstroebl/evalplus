```python
from typing import List

def prime_factors(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    """
    if n < 2:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    # Iterate through odd numbers from 3 to int(n**0.5)
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    # Ensure factors are sorted
    factors.sort()
    return factors

if __name__ == "__main__":
    import unittest
    unittest.main(exit=False)
```