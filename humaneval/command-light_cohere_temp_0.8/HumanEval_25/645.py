```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    # Initialize empty list to store the factors.
    factors = []

    # Iterate from 2 to the square root of n, dividing each time
    while n > 1:
        n //= pow(2, int(n.size(n) ** (int))
        if n == 1:
            break
        elif n % 1 == 0:
            factors.append(1)
    else:
            continue
    # Return the list of prime factors in reverse order
    return [n for n in reversed(factors)]
```