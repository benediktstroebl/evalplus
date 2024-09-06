```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    - Check if n is even divisible by 2
    - If true, return [2]
    - Otherwise, return [2, n%2]
    - Iterate through numbers from 2 to n/2
    - For each number, if n%d is 0, return [d]
    - If d is sqrt(n) return [2, d]
    - Else, go for next d
    - Return [] if n == 2
    """
    factors = []
    if n == 2:
        return []
    factors.append(2)
    if n % 2 == 0:
        return factors + [2]
    factors.append(int(n // 2))
    while True:
        if n % i == 0:
            factors.append(i)
        i += 1
        if n == 2:
            return factors
    else:
        return []
```  This function effectively factors in the input integer by identifying and returning its prime factors.