### Factorize Function
```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Returns a list of prime factors of the given integer in the order from smallest to largest.
    Each of the factors is listed the number of times corresponding to how many times it appears in factorization.
    
    Args:
    n (int): The number to factorize.
    
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
    while n > 1:
        if n % i == 0:
            n //= i
            factors.append(i)
        else:
            i += 1
    return factors

# Test the function
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This function uses a simple loop to divide the input number `n` by the smallest divisor `i` until `n` is no longer divisible by `i`. The divisor `i` is then added to the list of factors. This process continues until `n` is reduced to 1. The final list of factors represents the prime factorization of the input number.