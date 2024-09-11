### Prime Factorization
#### Python Script

```python
from typing import List

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
        if n % i == 0:
            factors.append(i)
            n = n // i
        else:
            i += 1
    return factors

# Example use cases
print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```

This script uses a simple iterative approach to find the prime factors of a given number. It starts from 2 and checks if the number is divisible by the current number. If it is, the factor is added to the list and the number is divided by the factor. This process continues until the number is reduced to 1. The remaining factors are all prime numbers. The script returns the list of prime factors in the order they appear.