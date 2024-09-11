```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The number to be factorized.

    Returns:
        List[int]: A list of prime factors.
    """
    factors = []
    divisor = 2
    while n > 1:
        # if n is divisible by divisor, it's a factor
        if n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        else:
            # else, increment divisor by 1
            divisor += 1
    return factors

# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```
This code works by dividing the input number `n` by the smallest divisor (2) as long as it's divisible. Then it increments the divisor until it finds the next number that can divide `n`. This process continues until `n` is reduced to 1. The list of divisors obtained through this process will be the list of prime factors of `n`.