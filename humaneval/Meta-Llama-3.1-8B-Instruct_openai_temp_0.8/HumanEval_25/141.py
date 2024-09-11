### Prime Factorization Script

```python
from typing import List
import math

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The number to factorize.

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
if __name__ == "__main__":
    print(factorize(8))  # [2, 2, 2]
    print(factorize(25))  # [5, 5]
    print(factorize(70))  # [2, 5, 7]
```

### Explanation

This script uses a simple trial division method to find the prime factors of a given integer `n`. It starts with the smallest prime number `2` and divides `n` by it as long as it's divisible. Then it increments the divisor until it finds the next number that can divide `n`. This process is repeated until `n` is reduced to 1. The list of divisors obtained during this process is the list of prime factors of `n`.