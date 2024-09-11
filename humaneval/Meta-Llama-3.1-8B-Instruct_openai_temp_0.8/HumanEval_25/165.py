```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    
    Args:
    n (int): The number to be factorized
    
    Returns:
    List[int]: A list of prime factors in the order from smallest to largest.
    """
    
    # Initialize an empty list to store prime factors
    factors = []

    # Initialize a divisor from 2 (smallest prime number)
    divisor = 2

    # Continue the loop until the number is reduced to 1
    while n > 1:
        # If the number is divisible by the current divisor
        while n % divisor == 0:
            # Append the divisor to the list of factors
            factors.append(divisor)
            # Divide the number by the divisor
            n = n // divisor
        # Move to the next divisor
        divisor += 1

    # Return the list of prime factors
    return factors

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script uses a simple trial division method to find the prime factors of the given number. It divides the number by the smallest divisor (2) as long as it is divisible, then increments the divisor and repeats the process until the number is reduced to 1. The list of prime factors is returned after the loop finishes.