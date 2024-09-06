```python
from typing import List
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Keep track of factors and counter while iterating through the numbers from 2 up to the square root of n.
    Factors: [2, 4, 6, 3]
    """
    factors = []
    while n > 1:
        if n % 2 == 0:
            factors.append(2)
            n = n // 2
        elif n % 3 == 0:
            factors.append(3)
            n = n // 3
        elif n % 5 == 0:
            factors.append(5)
            n = n // 5
        elif n % 7 == 0:
            factors.append(7)
            n = n // 7
        else:
            counter = 0
            square_root_n = int(math.sqrt(n))
            while square_root_n > 2 or counter >= 2:
                factors.append(counter)
                counter += 1
            else:
                factors.append(square_root_n)
                break
    return factors
```