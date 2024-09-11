### Factorization of an Integer
#### Problem Description
This script solves the task of factorizing a given integer into its prime factors. It returns a list of prime factors in the order from smallest to largest and with multiplicities.

#### Code
```python
from typing import List
import math

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    
    Args:
        n (int): The number to be factorized.
    
    Returns:
        List[int]: A list of prime factors of the given number.
    """
    factors = []
    divisor = 2
    
    # Iterate from 2 to the square root of n
    while n > 1:
        if n % divisor == 0:
            # If n is divisible by divisor, it's a prime factor
            exponent = 0
            while n % divisor == 0:
                n = n // divisor  # Divide n by divisor
                exponent += 1  # Increment the exponent

            # Append the prime factor with its exponent to the list
            factors.extend([divisor] * exponent)
        else:
            # If n is not divisible by divisor, increment divisor
            divisor += 1

    return factors

# Example usage:
print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```
This script uses a simple trial division method to find the prime factors of the given number. It iterates from 2 to the square root of the number and checks if the number is divisible by the current divisor. If it is, the divisor is a prime factor, and the script continues dividing the number by the divisor until it is no longer divisible. The prime factor is then added to the list with its corresponding exponent. The script continues this process until the number is reduced to 1.