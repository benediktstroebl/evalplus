```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Determine prime factors and keep track of their counts
    """
    factors = []
    counter = 1
    while n % 2 == 0:
        factors.append(2)
        counter += 1
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        counter += 1
        n = n // i
    for i in range(counter):
        factors.append(factors[i] * factors[i])[::-1]
    return factors
# Example test cases:
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```