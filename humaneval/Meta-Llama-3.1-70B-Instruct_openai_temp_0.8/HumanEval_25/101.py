```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    
    Args:
        n (int): The input number.

    Returns:
        List[int]: A list of prime factors.
    """
    factors = []
    divisor = 2

    # Continue dividing until the number is reduced to 1
    while n > 1:
        # If the number is divisible by the current divisor, add it to the factors list
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        # Increment the divisor by 1
        divisor += 1

    return factors


# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
print(factorize(100)) # [2, 2, 5, 5]
```

This script defines a function `factorize(n)` that takes an integer `n` as input and returns a list of its prime factors. It iteratively divides the input number by the smallest divisor (starting from 2) until the number is reduced to 1. The divisors are appended to the `factors` list in the order they appear. The function returns the `factors` list.

The test cases at the end of the script demonstrate the function's correctness for various inputs.