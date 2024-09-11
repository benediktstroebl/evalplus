### Prime Factorization Script

```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    
    Parameters:
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
        if n % i == 0:
            n = n // i
            factors.append(i)
        else:
            i += 1
    return factors

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize(n)` that takes an integer `n` as input and returns a list of its prime factors in the order from smallest to largest. The script uses a while loop to repeatedly divide the input number by the smallest divisor (starting from 2) until it is no longer divisible. The divisor is then added to the list of factors and the process repeats until the number is reduced to 1. The test cases at the end demonstrate the function's usage and correctness.