### Prime Factorization in Python
#### Problem Description
Given an integer `n`, return a list of prime factors of `n` in the order from smallest to largest. Each of the factors should be listed the number of times corresponding to how many times it appears in the factorization.

#### Solution

```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    
    Args:
        n (int): The input number.
    
    Returns:
        List[int]: A list of prime factors of `n`.
    
    Example:
        >>> factorize(8)
        [2, 2, 2]
        >>> factorize(25)
        [5, 5]
        >>> factorize(70)
        [2, 5, 7]
    """
    factors = []
    i = 2
    while n > 1:
        # Check for divisibility from 2 to sqrt(n)
        while n % i == 0:
            # If the current number is divisible, add it to the factors list and divide n by it
            factors.append(i)
            n = n // i
        # Move to the next number
        i += 1
    return factors

# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```
This script defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors. The function uses a while loop to check for divisibility of `n` by all numbers from 2 to the square root of `n`. If `n` is divisible by a number `i`, it adds `i` to the list of factors and divides `n` by `i`. This process continues until `n` is reduced to 1. The function then returns the list of factors.