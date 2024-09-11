```python
from typing import List
import math

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    
    Args:
        n (int): The number to factorize.
    
    Returns:
        List[int]: A list of prime factors of the input number.
    """
    
    # Initialize an empty list to store the prime factors
    factors = []
    
    # Handle the special case when the input number is 1
    if n == 1:
        return factors
    
    # Find the smallest prime factor
    i = 2
    while i * i <= n:
        if n % i:
            # If 'i' is not a factor, increment it by 1
            i += 1
        else:
            # If 'i' is a factor, increment its count and divide 'n' by 'i'
            n //= i
            factors.append(i)
    
    # If 'n' is a prime number greater than 1, append it to the factors list
    if n > 1:
        factors.append(n)
    
    # Return the list of prime factors
    return factors

# Test the function
print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
print(factorize(1))  # Output: []
```

This script defines the `factorize` function, which takes an integer `n` as input and returns a list of its prime factors. It iteratively finds the smallest prime factor of `n` and divides `n` by it until it can no longer be divided. If the remaining `n` is a prime number greater than 1, it is added to the list of factors. The function returns the list of prime factors. The script also includes test cases to verify the correctness of the `factorize` function.