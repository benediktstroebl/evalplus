```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    
    Args:
        n (int): The number to be factored.
    
    Returns:
        List[int]: A list of prime factors.
    
    Example:
        >>> factorize(8)
        [2, 2, 2]
        >>> factorize(25)
        [5, 5]
        >>> factorize(70)
        [2, 5, 7]
    """
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# Test the function
print(factorize(8))   # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```

This script defines a function called `factorize` that takes an integer `n` as input and returns a list of its prime factors. The function uses a while loop to iterate from 2 to the square root of `n`, checking for divisibility. If `n` is divisible by `i`, it is divided by `i` and `i` is added to the list of factors. This process continues until `n` is reduced to 1. If `n` is a prime number greater than 1, it is added to the list of factors. Finally, the function returns the list of factors.

The test cases at the end demonstrate how to call the `factorize` function with different inputs and print the results.