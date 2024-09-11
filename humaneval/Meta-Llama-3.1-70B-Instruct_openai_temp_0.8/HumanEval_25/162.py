```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    
    Args:
        n (int): Input number to be factorized.
    
    Returns:
        List[int]: A list of prime factors.
    """
    # Initialize an empty list to store prime factors
    factors = []
    
    # Initialize divisor to 2 (smallest prime number)
    divisor = 2
    
    # Continue the loop while n is greater than 1
    while n > 1:
        # Check if n is divisible by divisor
        if n % divisor == 0:
            # If divisible, append divisor to factors list
            factors.append(divisor)
            # Update n by dividing it with divisor
            n = n // divisor
        else:
            # If not divisible, increment divisor by 1
            divisor += 1
    
    return factors

# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This Python script uses a simple trial division method to find the prime factors of a given number. It starts by checking divisibility from the smallest prime number (2) and keeps incrementing the divisor until it finds a factor. The process continues until the input number is reduced to 1. The prime factors are stored in a list and returned as the result.