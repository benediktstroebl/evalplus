```python
from typing import List


def prime_factors(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    
    :param n: Input integer to factorize
    :return: List of prime factors
    """
    
    # Initialize an empty list to store prime factors
    factors = []
    
    # Start dividing the number from 2
    i = 2
    
    # Continue until the number is reduced to 1
    while n > 1:
        # If the number is divisible by the current divisor, it's a prime factor
        if n % i == 0:
            # Append the factor to the list
            factors.append(i)
            # Divide the number by the factor
            n = n // i
        else:
            # If the number is not divisible, increment the divisor by 1
            i += 1
    
    # Return the list of prime factors
    return factors


# Test the function
print(prime_factors(8))  # [2, 2, 2]
print(prime_factors(25))  # [5, 5]
print(prime_factors(70))  # [2, 5, 7]
```

This script defines a function `prime_factors` that takes an integer `n` as input and returns a list of its prime factors in the order from smallest to largest. The function iteratively divides the number by the smallest divisor (starting from 2) until it's reduced to 1. Each divisor that divides the number is considered a prime factor and is added to the list. The function returns the list of prime factors.