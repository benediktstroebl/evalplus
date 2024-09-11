```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    
    Args:
    n (int): The number to factorize.
    
    Returns:
    List[int]: A list of prime factors.
    """
    
    # Initialize an empty list to store the prime factors
    factors = []
    
    # Initialize the divisor to 2, the smallest prime number
    divisor = 2
    
    # While the number is greater than 1, keep dividing it by the divisor
    while n > 1:
        
        # While the number is divisible by the divisor, add the divisor to the list of factors
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        
        # Move to the next number that could be a divisor
        divisor += 1
    
    return factors

# Test the function
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize(n)` that takes an integer `n` as input and returns a list of its prime factors. The function uses a while loop to divide the input number by the smallest divisor (starting from 2) as long as it is divisible. The divisor is then incremented, and the process is repeated until the number is reduced to 1. The list of factors is then returned. The script includes test cases to demonstrate the function's correctness.