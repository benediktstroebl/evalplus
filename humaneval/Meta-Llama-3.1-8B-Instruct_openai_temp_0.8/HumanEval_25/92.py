### Prime Factorization in Python
#### Script
```python
from typing import List

def prime_factorize(n: int) -> List[int]:
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
            # If i is a factor, add it to the list and divide n by i
            factors.append(i)
            n = n // i
        else:
            # If i is not a factor, increment i by 1
            i += 1
    return factors

# Test cases
print(prime_factorize(8))  # [2, 2, 2]
print(prime_factorize(25))  # [5, 5]
print(prime_factorize(70))  # [2, 5, 7]
```
#### Explanation
This script defines a function `prime_factorize` that takes an integer `n` as input and returns a list of its prime factors. The function uses a while loop to divide `n` by the smallest possible factor (starting from 2) until `n` is reduced to 1. If `n` is divisible by the current factor `i`, it is added to the list of factors and `n` is divided by `i`. If `n` is not divisible by `i`, `i` is incremented by 1. This process continues until `n` is reduced to 1. The resulting list of factors is returned.