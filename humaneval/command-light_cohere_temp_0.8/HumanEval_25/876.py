```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Keep track of factors collected so far, starting from 2, and the next one should be a factor if its multiplication doesn't create a number greater than n.
    Steps:
    - Initialize list with 2 and n
    - Start loop and while loop until sqrt(n)
    - Multiply current factor with next factor and add it to the list
    - Calculate sqrt(n) using math.sqrt()
   
    note that this is to be calculated inside a loop
    - If sqrt(n) > 2, return list with only n
    - Else, start the loop with step 2 above
    - Else, return list with current factors and n
    """
    factors = [2]
    while n % 2 == 0:
        factors.append(n //
   
        n // 2 == 1
        n = n // 2
    while len(factors) < sqrt(n) + 1:
        for i in range(3, int(n ** 0.5) + 1, while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors
```