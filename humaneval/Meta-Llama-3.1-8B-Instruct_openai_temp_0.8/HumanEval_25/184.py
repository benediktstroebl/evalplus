### Factorize Function
#### Python Script
```markdown
from typing import List
import math

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The integer to factorize.

    Returns:
        List[int]: A list of prime factors of the given integer.
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

This script uses a simple trial division method to find the prime factors of a given integer. It starts by dividing the number by 2 and then increments the divisor until it finds a factor. Once it finds a factor, it continues dividing the number by that factor until it is no longer divisible. It repeats this process until the number is reduced to 1. The list of factors is then returned.