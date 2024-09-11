### Prime Factorization Script
#### Code

```python
from typing import List
import math


def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    
    Args:
        n (int): The number to factorize.
    
    Returns:
        List[int]: A list of prime factors of the given number.
    """
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

#### Explanation

This script implements a function `factorize(n)` that takes an integer `n` as input and returns a list of prime factors of `n`. The function uses a while loop to iterate over all numbers from 2 to the square root of `n`. If `n` is divisible by the current number `i`, `n` is divided by `i` and `i` is appended to the list of factors. This process is repeated until `n` is reduced to 1. If `n` is a prime number greater than 1, it is appended to the list of factors at the end.