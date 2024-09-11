```python
from typing import List
import math

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The number to be factorized

    Returns:
        List[int]: A list of prime factors of the given integer
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    # Check for other odd factors
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i

    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)

    return factors

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script uses a simple iterative approach to find the prime factors of a given integer. It starts by checking if the number is divisible by 2, and if so, it keeps dividing the number by 2 until it's no longer divisible. Then, it checks for other odd factors by iterating from 3 to the square root of the number. If the number is a prime number greater than 2, it's appended to the list of factors. The function returns the list of factors.