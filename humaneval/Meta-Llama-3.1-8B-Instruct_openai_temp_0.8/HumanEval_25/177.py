```python
from typing import List
import math

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    
    Args:
    n (int): Input number to be factorized.
    
    Returns:
    List[int]: A list of prime factors of the input number.
    """
    
    # Initialize an empty list to store the prime factors
    factors = []
    
    # Find the square root of the number
    sqrt_n = math.isqrt(n)
    
    # Iterate from 2 to the square root of the number
    for i in range(2, sqrt_n + 1):
        
        # Check if the number is divisible by the current number
        while n % i == 0:
            # If it is, add the current number to the list of factors
            factors.append(i)
            # Divide the number by the current number
            n = n // i
            
    # If the remaining number is greater than 1, it is a prime number
    if n > 1:
        # Add the remaining number to the list of factors
        factors.append(n)
    
    # Return the list of prime factors
    return factors


# Test cases
if __name__ == "__main__":
    print(factorize(8))  # [2, 2, 2]
    print(factorize(25))  # [5, 5]
    print(factorize(70))  # [2, 5, 7]
```

This script works by iterating from 2 to the square root of the input number, and at each step, it checks if the number is divisible by the current number. If it is, it adds the current number to the list of factors and divides the number by the current number. This process is repeated until the number is reduced to 1, at which point the list of factors is returned. If the remaining number is greater than 1, it is added to the list of factors as it is a prime number.