```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Returns list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times corresponding to how many times it appears in factorization.
    """
    factor(8) returns [2, 2, 2]
    """
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)
    while n >= 2 and n % i == 0:
        n /= i
        factors.append(i)
    return factors
```
The function factors out all the prime factors of the number n, in order from the smallest prime factor to the largest prime factor. The function uses a iterative method to factorize the number.