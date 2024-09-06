```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest
    Each of them is listed number of times which they appear in factorization
    of given number
    Input number should be equal to the product of all factors
    """
    factors = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
        factors.append(i)
        n //= i
    factors.append(n)
    return factors
```
The function identifies prime factors of a given number and returns them in descending order. Each factor is listed number of times it appears in the factorization of the given number.