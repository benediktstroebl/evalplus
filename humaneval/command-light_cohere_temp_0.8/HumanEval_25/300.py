```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times, which corresponds to how many times it appears in factorization
    Input number should be equal to the product of all its factors
    """
    if n < 2:
        raise ValueError("Input number must be positive and greater than 1")
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5, 2)::
        while n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(n)
    return factors
```
The function factorize in this script returns a list of prime factors of the input integer n in ascending order. Each factor is listed number of times which it appears in factorization, as dictated by the function. The function also incorporates a condition that the input number must be positive and greater than 1, and raises a ValueError if this condition is not met.