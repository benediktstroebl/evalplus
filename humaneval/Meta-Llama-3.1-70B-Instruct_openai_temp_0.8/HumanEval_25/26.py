```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    :param n: The number to be factorized
    :return: A list of prime factors
    """
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        divisor += 1
    return factors

# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script works by dividing the input number `n` by the smallest divisor (which starts at 2), and appending that divisor to the list of factors as many times as it is divisible. The divisor is then incremented, and the process is repeated until `n` is reduced to 1. The list of factors is then returned.