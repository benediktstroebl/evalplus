### Factorize Function
```python
from typing import List
import math

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The number to be factorized.

    Returns:
        List[int]: A list of prime factors.
    """
    factors = []
    i = 2
    while n > 1:
        # Check if i is a factor of n
        if n % i == 0:
            # If i is a factor, divide n by i and increment i
            n = n // i
            factors.append(i)
        else:
            # If i is not a factor, increment i by 1
            i += 1
    return factors

# Test cases
print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```
This script defines a function `factorize(n)` that takes an integer `n` as input and returns a list of its prime factors. The function uses a while loop to continuously divide `n` by the smallest prime factor until `n` is reduced to 1. The prime factors are then returned as a list. The test cases demonstrate the function's correctness by verifying that the output matches the expected output for various inputs.