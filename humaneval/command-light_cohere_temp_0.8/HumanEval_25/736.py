```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times, which corresponds to how many times the factor appears in the factorization of the number.
    Input number should be equal to the product of all factors
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    for j in range(int(n**0.5) + 1, while n % j == 0 and j != i:
        factors.append(j)
        n = n // j
    return factors

# Example usage:
print(factorize(8))
print(factorize(25))
print(factorize(70))
```