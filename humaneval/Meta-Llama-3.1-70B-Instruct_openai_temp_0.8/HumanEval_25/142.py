```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    """
    # Initialize an empty list to store the prime factors
    factors = []
    
    # Initialize a divisor to 2 (the smallest prime number)
    divisor = 2
    
    # Continue the loop until the number is completely factorized
    while n > 1:
        # If the number is divisible by the current divisor, it is a prime factor
        if n % divisor == 0:
            # Add the divisor to the list of factors
            factors.append(divisor)
            # Divide the number by the divisor to move to the next factor
            n = n // divisor
        else:
            # If the number is not divisible by the current divisor, increment the divisor by 1
            divisor += 1
    
    # Return the list of prime factors
    return factors


# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize(n)` that takes an integer `n` as input and returns a list of its prime factors. The function iteratively divides the input number by the smallest divisor until it is no longer divisible, then increments the divisor and repeats the process. The list of divisors is returned as the list of prime factors. The test cases at the end of the script demonstrate the function's correctness.