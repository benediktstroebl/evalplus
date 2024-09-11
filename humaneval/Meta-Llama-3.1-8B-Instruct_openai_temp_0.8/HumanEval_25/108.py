### Prime Factorization Script
```markdown
## Description
This script provides a function `factorize` that calculates the prime factors of a given integer.
The prime factors are returned in a list, ordered from smallest to largest, and each factor appears in the list as many times as it appears in the factorization of the input number.

## Requirements
- Python 3.x

## Code
```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    
    Args:
        n (int): The input number to factorize.
    
    Returns:
        List[int]: A list of prime factors of the input number.
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

# Example usage
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```
### Explanation
The `factorize` function uses a loop to divide the input number `n` by increasing integers `i`. If `n` is divisible by `i`, it is divided by `i` and the result is appended to the list of factors. This process continues until `i` is greater than the square root of `n`. If `n` is not divisible by `i` at any point, `i` is incremented. Finally, if `n` is greater than 1 after the loop, it is also appended to the list of factors as it is a prime factor.