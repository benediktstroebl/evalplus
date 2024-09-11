```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    
    Args:
    n (int): The input number to be factorized.
    
    Returns:
    List[int]: A list of prime factors of the input number.
    
    Examples:
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    
    # Initialize an empty list to store prime factors
    factors = []
    
    # Initialize a variable to divide the input number
    divisor = 2
    
    # Continue dividing the input number until it's reduced to 1
    while n > 1:
        # If the input number is divisible by the divisor, it's a prime factor
        while n % divisor == 0:
            # Add the prime factor to the list
            factors.append(divisor)
            # Divide the input number by the prime factor
            n = n // divisor
        # If the input number is not divisible by the divisor, increment the divisor
        divisor += 1
        
        # If the divisor is greater than the square root of the input number, 
        # it's no longer a valid divisor, so we can stop the loop
        if divisor * divisor > n:
            if n > 1:  # in case of prime number
                factors.append(n)  # add n if it is prime
            break
    
    # Return the list of prime factors
    return factors

# Example usage:
print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```