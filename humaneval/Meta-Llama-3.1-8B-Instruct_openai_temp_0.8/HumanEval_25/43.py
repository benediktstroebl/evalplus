```python
from typing import List
import math


def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    
    Parameters:
    n (int): The number to be factorized
    
    Returns:
    List[int]: A list of prime factors of n
    """
    factors = []
    i = 2
    while i * i <= n:
        # Check if i is a factor of n
        if n % i:
            # If not, increment i by 1
            i += 1
        else:
            # If i is a factor, divide n by i and increment i
            n //= i
            factors.append(i)
    # If n is a prime number greater than 1, it is a factor of the original number
    if n > 1:
        factors.append(n)
    return factors


# Test cases
print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```

This script defines a function `factorize(n)` that takes an integer `n` as input and returns a list of its prime factors in the order from smallest to largest. The function uses a while loop to check for factors starting from 2 and increments the potential factor until it finds one that is a factor or until the square of the potential factor is greater than the input number. The input number is divided by the found factor, and the factor is added to the list of factors. This process repeats until the input number is reduced to 1. If the remaining number is a prime number greater than 1, it is also added to the list of factors. The test cases at the end demonstrate the function's correctness.