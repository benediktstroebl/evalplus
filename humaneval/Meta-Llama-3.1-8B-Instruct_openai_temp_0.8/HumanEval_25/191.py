```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    
    Parameters:
    n (int): The number to factorize.
    
    Returns:
    List[int]: A list of prime factors of the input number.
    """
    
    # Initialize an empty list to store prime factors
    factors = []
    
    # Initialize a variable to divide the input number
    i = 2
    
    # Continue the loop until the input number is fully divided
    while n > 1:
        # Check if the current number is a factor of the input number
        if n % i == 0:
            # If it is, add it to the list of factors and divide the input number by the current factor
            factors.append(i)
            n = n // i
        else:
            # If it's not, increment the current number by 1
            i += 1
    
    # Return the list of factors
    return factors

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```