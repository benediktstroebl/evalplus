### Prime Factorization Script
```python
from typing import List
import math

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    
    Args:
        n (int): The input integer to be factorized.
    
    Returns:
        List[int]: A list of prime factors of the input integer.
    
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
        # Check if i is a factor of n
        if n % i == 0:
            # If i is a factor, add it to the list and divide n by i
            factors.append(i)
            n = n // i
        else:
            # If i is not a factor, increment i by 1
            i += 1
    return factors

# Test the function
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```
This script uses a simple algorithm to find the prime factors of a given integer. It iterates over all numbers from 2 to n (inclusive), checking if each number is a factor of n. If it is, it adds the number to the list of factors and divides n by that number. This process continues until n is reduced to 1. The resulting list of factors is then returned.