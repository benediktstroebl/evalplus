```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    
    Args:
        n (int): The number to factorize
    
    Returns:
        List[int]: The list of prime factors of n
    
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

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize(n)` that returns a list of prime factors of `n`. It uses a simple trial division method, which for each number from 2 up to the square root of `n` checks whether `n` is divisible by it. If it is, then it keeps dividing `n` by the divisor until `n` is no longer divisible by it. The divisor is then added to the list of factors. This process is repeated until `n` is reduced to 1. The remaining value of `n` (if any) is also added to the list of factors (since it's a prime factor). The function finally returns the list of factors.