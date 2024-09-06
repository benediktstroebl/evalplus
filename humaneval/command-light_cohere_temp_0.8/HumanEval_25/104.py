```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are returned number of times, which corresponds to how many times it appears in the factorization.
    Input number should be equal to the product of all factors
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n = n // i
        i += 1
    for num in factors:
        factors.append(num) * 2
    return factors
```
This function does prime factorization for the given number, and returns the list of prime factors in order from smallest to largest. 

Please note that this is a very basic implementation, and can be improved in many ways.