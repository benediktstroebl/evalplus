```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    
    :param n: The number to be factorized
    :return: A list of prime factors
    """
    
    # Initialize an empty list to store prime factors
    factors = []
    
    # Initialize divisor to 2 (smallest prime number)
    divisor = 2
    
    # Continue loop until n is greater than 1
    while n > 1:
        # If n is divisible by divisor, it is a prime factor
        if n % divisor == 0:
            # Append divisor to the list of factors
            factors.append(divisor)
            # Divide n by divisor to remove this factor
            n = n // divisor
        else:
            # If n is not divisible by divisor, increment divisor by 1
            divisor += 1
    
    # Return the list of prime factors
    return factors


# Test cases
print(factorize(8))   # Expected output: [2, 2, 2]
print(factorize(25))  # Expected output: [5, 5]
print(factorize(70))  # Expected output: [2, 5, 7]
```

This script defines a function `factorize` that takes an integer `n` as input and returns a list of prime factors. It iteratively divides `n` by the smallest divisor (starting from 2) until `n` is reduced to 1. The divisors that divide `n` are appended to the list of factors. The function returns the list of prime factors.