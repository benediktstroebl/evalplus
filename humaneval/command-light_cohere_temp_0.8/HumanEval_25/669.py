```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times corresponding to how many times it appears in factorization of the number
    Input number should be a product of all its factors
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5), n //1):
        while n % i == 0:
        factors.append(i)
        n = n // i
    factors.append(n)
    return factors
```
The function `factorize` takes an integer `n` as input and returns a list of prime factors of `n` in ascending order, with each factor listed according to how many times it appears in the factorization of `n`.