```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times which corresponds to how many times it appears in factorization
    Input number should be equal to the product of all its factors
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
        n = n // 2
    for i in range(3, int(n**0.5, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    factors.append(int)
    return factors
```
This script defines a function `factorize` that takes an integer `n` as input and returns a list of prime factors of `n` in order from smallest to largest. The function uses a loops to find the prime factors of `n` and their corresponding number of times they appear in factorization.