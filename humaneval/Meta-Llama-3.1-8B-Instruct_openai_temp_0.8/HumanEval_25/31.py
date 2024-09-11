```python
from typing import List
import math

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The number to be factorized

    Returns:
        List[int]: A list of prime factors in the order from smallest to largest
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

This script defines a function `factorize(n)` that takes an integer `n` as input and returns a list of its prime factors in the order from smallest to largest. The function uses a while loop to divide `n` by the smallest prime number (i.e., 2) as long as it's divisible, then increments the divisor until it finds the next number that can divide `n`. This process is repeated until `n` is reduced to 1. If at any point `n` is not divisible by the current divisor, the divisor is incremented. If `n` is greater than 1 at the end of the loop, it means that `n` is a prime number and is added to the list of factors. The function returns the list of factors.