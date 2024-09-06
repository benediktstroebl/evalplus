```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    If a list comprehension that iterates through numbers from 2 up to the power of sqrt(n)
    and checks whether it is divisible by n.
    """
    list(range(2, int(math.sqrt(n))+1))
    # we can replace int(math.sqrt(n)) with n // (n is always positive)
    """
    factors = []
    for x in range(2, int(math.sqrt(n))+1):
        if n % x == 0:
            factors.append(x(x)
            factors.append(factors[-1])
            factors.remove(x)
            factors[0] = factors.remove(factors[0] * x)
    factors.append(x(x))
    return factors
```
This function takes an integer n as input and returns a list of prime factors of n in descending order, along with the count of each factor. It does so by iterating through numbers from 2 to the square root of n, and checking whether n is divisible by each number. Once a number is found that satisfies this condition, it's added to the list of factors and the number itself is removed from the list of factors. The number one is added back to the list to maintain the order of factors.