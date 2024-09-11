### Prime Factorization of an Integer
#### Python Script
```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    
    Args:
        n (int): Input integer for prime factorization
    
    Returns:
        List[int]: List of prime factors in the order from smallest to largest
    """
    factors = []
    i = 2
    while n > 1:
        # Check if i is a factor of n
        if n % i == 0:
            # If i is a factor, add it to the list of factors and divide n by i
            factors.append(i)
            n = n // i
        else:
            # If i is not a factor, increment i by 1
            i += 1
    
    return factors

# Example usage:
print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```
This script defines a function `factorize(n)` that takes an integer `n` as input and returns a list of its prime factors. The function uses a while loop to iterate from 2 to `n` and checks if each number is a factor of `n`. If it is, the factor is added to the list and `n` is divided by the factor. This process continues until `n` is reduced to 1. The resulting list of factors is then returned.