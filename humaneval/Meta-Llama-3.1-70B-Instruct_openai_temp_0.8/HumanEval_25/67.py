Here is a self-contained Python script that solves the problem:
```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    
    Args:
        n (int): Input number to be factorized
    
    Returns:
        List[int]: List of prime factors
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
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```
This script defines a function `factorize` that finds the prime factors of a given integer `n`. The function iterates through numbers from 2 to the square root of `n`, checks if `n` is divisible by the current number, and if it is, appends the number to the list of factors and divides `n` by the number. If `n` is still greater than 1 after the loop, it means `n` itself is a prime factor, so it is appended to the list. Finally, the function returns the list of prime factors. The script includes test cases to verify the correctness of the function.