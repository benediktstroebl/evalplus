```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Input number: n -->
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1,):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors
```
This Python function, factorize, calculates and returns a list of prime factors for the given integer n, ordered from smallest to largest. The function employs the technique of factoring by squaring and trial division, checking for divisibility until reaching factors greater than the square root of n. 

The function is self-contained, efficiently solving the prime factorization problem for a wide range of input integers without depending on external libraries or recursion.