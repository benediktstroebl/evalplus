### Prime Factorization Script

```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors.
    
    Args:
    n (int): Integer to be factorized
    
    Returns:
    List[int]: List of prime factors in the order from smallest to largest.
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
if __name__ == "__main__":
    print(factorize(8))  # Output: [2, 2, 2]
    print(factorize(25))  # Output: [5, 5]
    print(factorize(70))  # Output: [2, 5, 7]
```

This script defines a function `factorize(n)` that takes an integer `n` as input and returns a list of its prime factors. The function uses a simple algorithm to find the prime factors, starting from the smallest prime number (2). It continues to divide `n` by the current factor until it is no longer divisible, adding the factor to the list each time. This process is repeated until `n` is reduced to 1. If `n` is a prime number greater than 1, it is added to the list at the end. The test cases at the end of the script demonstrate the function's behavior with the inputs 8, 25, and 70.