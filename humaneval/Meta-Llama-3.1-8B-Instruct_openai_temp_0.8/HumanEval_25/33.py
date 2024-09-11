```python
from typing import List
import math

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
    n (int): The number to factorize

    Returns:
    List[int]: A list of prime factors
    """
    factors = []
    divisor = 2
    while n > 1:
        # While n is divisible by divisor, add it to factors list and divide n
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        # If n is not divisible by divisor, increment divisor until it is
        divisor += 1
        # We can break the loop if divisor exceeds sqrt(n) because a larger factor of n must be a multiple of a smaller factor that has already been accounted for.)
        if divisor > math.sqrt(n):
            if n > 1:  # if n itself is a prime number greater than square root of n
                factors.append(n)
                break
    return factors

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

In this script, we define a function `factorize(n)` that takes an integer `n` as input and returns a list of its prime factors. The function uses a while loop to divide `n` by the smallest divisor that divides it, repeatedly, until `n` is reduced to 1. The divisors are added to the `factors` list as they are encountered, and the loop continues until `n` is reduced to 1. The function returns the `factors` list. The test cases are used to verify the correctness of the function.