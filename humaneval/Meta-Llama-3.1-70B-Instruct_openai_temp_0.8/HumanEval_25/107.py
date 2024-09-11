```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors

    Args:
    n (int): The number to factorize.

    Returns:
    List[int]: A list of prime factors.
    """
    
    # Initialize an empty list to store prime factors
    factors = []
    
    # Initialize divisor to 2 (smallest prime number)
    divisor = 2
    
    # Continue loop until n is reduced to 1
    while n > 1:
        # If n is divisible by divisor, it's a prime factor
        while n % divisor == 0:
            # Append divisor to factors list
            factors.append(divisor)
            # Divide n by divisor
            n = n // divisor
        # Increment divisor by 1
        divisor += 1
    
    # Return list of prime factors
    return factors


# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```
In this Python script, the function `factorize(n)` takes an integer `n` as input and returns a list of its prime factors. It works by iterating from 2 (the smallest prime number) up to `n`, and for each number, it checks if it's a divisor of `n`. If it is, it's a prime factor, so it's added to the list and `n` is divided by it. This continues until `n` is reduced to 1, at which point all prime factors have been found.