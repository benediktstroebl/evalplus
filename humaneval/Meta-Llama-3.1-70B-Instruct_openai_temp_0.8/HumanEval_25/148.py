```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    
    :param n: The number to factorize
    :return: List of prime factors
    """
    factors = []
    divisor = 2

    # Keep dividing the number until it's no longer divisible by the current divisor
    while n > 1:
        # If the number is divisible by the current divisor, add it to the list and divide the number
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        # Otherwise, increment the divisor
        divisor += 1

    return factors


# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
print(factorize(100)) # [2, 2, 5, 5]
```