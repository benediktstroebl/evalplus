```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    # Loop through through the times the factors and check for divisibility
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            factors.append(i)
            factors.append(i) # on each subsequent even (to make sure the list is ordered)
    factors.append(i)
    """ factors, each one number of times
    """

# Test cases
print(factorize(8))
print(factorize(25))
print(factorize(70))
```