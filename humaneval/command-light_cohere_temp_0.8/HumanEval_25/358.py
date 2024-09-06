```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times corresponding to how many times it appears in factorization
    Input number should be equal to the product of all the factors returned
    """
    factors = []
    while n % 2 == 0:
        n = n / 2
        factors.append(2)
    factors.append(n)
   
    while n > 1:
        for i in range(2, int(n**0.5) + 1):
            n = n / i
            factors.append(i)
    factors.append(n)
    return factors
```
The function returns the list of prime factors in order from the smallest to the largest. The factors are listed in the number of times they appear in the factorization.