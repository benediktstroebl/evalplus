```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    - Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    - Input number should be equal to the product of all factors
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5)+1,  while n % i == 0:
        factors.append(i)
        n = n // i
    return factors

# Tests
print(factorize(8))      # [2, 2, 2]
print(factorize(25))    # [5, 5]
print(factorize(70))    # [2, 5, 7]
``` 
This script defines a function that returns a list of prime factors of a given integer in order from smallest to largest. It uses a iterative approach to find factors and ensures that each factor is listed number of times corresponding to how many times it appears in factorization. The script also includes tests to ensure the function is working correctly for the provided inputs.