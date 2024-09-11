```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    
    Args:
        n (int): The input number to be factorized.
    
    Returns:
        List[int]: A list of prime factors.
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

This script works by continuously dividing the input number `n` by the smallest prime number (which starts at 2) until it is no longer divisible. The divisor is then added to the list of factors, and the process repeats until `n` is reduced to 1. If `n` is greater than 1 at the end of the loop, it means that `n` is a prime number and is added to the list of factors. The loop only needs to go up to the square root of `n` because a larger factor of `n` would be a multiple of a smaller factor that has already been checked.