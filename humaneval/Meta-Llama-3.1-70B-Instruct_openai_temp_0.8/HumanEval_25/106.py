```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    
    Args:
        n (int): The input number to factorize.
    
    Returns:
        List[int]: A list of prime factors.
    """
    
    # Initialize an empty list to store the prime factors
    factors = []
    
    # Initialize the divisor to 2, which is the smallest prime number
    divisor = 2
    
    # Continue the loop until the number is completely factorized
    while n > 1:
        # Check if the number is divisible by the current divisor
        if n % divisor == 0:
            # If it is, add the divisor to the list of factors
            factors.append(divisor)
            # Divide the number by the divisor
            n = n // divisor
        else:
            # If the number is not divisible by the current divisor, increment the divisor by 1
            divisor += 1
    
    return factors

# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize` that takes an integer `n` as input and returns a list of prime factors in the order from smallest to largest. Each factor is listed the number of times it appears in the factorization. The function uses a simple trial division method to find the prime factors. It starts with the smallest prime number (2) and checks if the number is divisible by the current divisor. If it is, the divisor is added to the list of factors and the number is divided by the divisor. This process continues until the number is completely factorized.