```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    
    Args:
        n (int): The number to be factorized
    
    Returns:
        List[int]: A list of prime factors
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

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize` that takes an integer `n` and returns a list of its prime factors in ascending order. The function uses a while loop to check each potential factor up to the square root of `n`. If `n` is divisible by the current potential factor, it is divided out and added to the list of factors. This process continues until `n` is reduced to 1, at which point all factors have been found. The function then returns the list of factors.

The script also includes some test cases to demonstrate the function's usage.