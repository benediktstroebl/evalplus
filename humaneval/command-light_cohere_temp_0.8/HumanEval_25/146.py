```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Retrieving prime factors:
    1. Identify all numbers less equal n to reach divisibility threshold
    2. Filter out all but one number (threshold) from the list, which is guaranteed to be a prime
    3. Calculate the factor of remaining numbers: multiply each remaining number with the largest number, and take only the highest result, as it represents the largest factor
    4. Repeat steps 2 until there numbers reach 0
    5. Repeat step 3 until all numbers have become 0
    6. Identify the resulting prime factor list
   
    """
    if n <= 1:
        return []
    elif n <= 3:
        return [1]
    elif n % 2 == 0 or n % 3 == 0:
        return [2] + factorize(n // 3)
    else:
        for i in range(5, n // 2 + 1, -1):
            if n % i == 0:
                return [i] + factorize([n // i])
        return []
```