### Factorization of an Integer
#### Problem Statement
Given an integer `n`, return a list of its prime factors ordered from smallest to largest. Each factor should be listed the number of times it appears in the factorization.

#### Solution
```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    
    Parameters:
    n (int): Input integer to be factorized
    
    Returns:
    List[int]: List of prime factors ordered from smallest to largest
    
    Examples:
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# Example usage:
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors. The function uses a while loop to iterate from 2 to the square root of `n`. If `n` is divisible by the current number `i`, it divides `n` by `i` and appends `i` to the factors list. If `n` is not divisible by `i`, it increments `i` by 1. If `n` is greater than 1 after the loop, it means `n` is a prime number and is appended to the factors list. Finally, the function returns the list of factors.