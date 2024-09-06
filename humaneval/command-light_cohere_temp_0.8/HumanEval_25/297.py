```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors
```
This script defines a function called `factorize` that takes an integer `n` as input and returns a list of prime factors of `n` in order from smallest to largest. The function works by first checking for the number 2, which is the only even prime factor. Then, it checks for other prime factors by iterating through the list of prime numbers, starting from 3 up to the square root of the number.

Finally, it returns the list of prime factors of the given number.