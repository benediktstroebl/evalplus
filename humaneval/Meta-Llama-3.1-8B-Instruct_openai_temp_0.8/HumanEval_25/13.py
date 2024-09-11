### Prime Factorization of a Number
#### Problem Description
Create a Python function `factorize` that takes an integer `n` as input and returns a list of its prime factors in the order from smallest to largest.

#### Code Solution

```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    
    Args:
        n (int): The number to be factorized.
    
    Returns:
        List[int]: A list of prime factors.
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

#### Explanation
This function `factorize` uses a simple trial division method to find the prime factors of a number. It iteratively divides the input number `n` by the smallest prime number `i` (initially 2) as long as it's divisible. If `n` is not divisible by `i`, it increments `i` by 1. If `n` is reduced to 1, it means all its prime factors have been found and are stored in the `factors` list. The function finally returns the list of prime factors.