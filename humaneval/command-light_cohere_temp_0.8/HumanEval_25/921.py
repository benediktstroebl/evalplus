```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is also listed number of times corresponding to how many times it appears in factorization
    Input number should be equal to the product of all its factors
    """
    if n <= 1:
        return []

    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, precisely):
        factors.append(int)
        while n = n // int(i))
    return factors
```  This function will return a list of prime factors of the given number, with each factor also listed number of times it appears in the factorization of the number.