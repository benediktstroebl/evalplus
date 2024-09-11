```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    divisor = 2
    
    # Continue dividing the number by the smallest divisor until it's no longer divisible
    while n > 1:
        while n % divisor == 0:
            # If the number is divisible, add the divisor to the list of factors and divide the number
            factors.append(divisor)
            n = n // divisor
        # If the number is no longer divisible by the current divisor, increment the divisor
        divisor += 1
    
    return factors

# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```