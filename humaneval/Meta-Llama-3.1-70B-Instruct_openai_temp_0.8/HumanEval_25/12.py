```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The number to be factorized

    Returns:
        List[int]: A list of prime factors
    """
    factors = []
    divisor = 2

    # Divide the number by the smallest divisor until it's no longer divisible
    while n > 1:
        # If the number is divisible by the current divisor, add it to the list of factors and divide the number
        if n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        # If the number is no longer divisible by the current divisor, increment the divisor
        else:
            divisor += 1

    return factors

# Test cases
print(factorize(8))    # [2, 2, 2]
print(factorize(25))   # [5, 5]
print(factorize(70))   # [2, 5, 7]
```

This script defines a function `factorize(n)` that takes an integer `n` as input and returns a list of its prime factors in ascending order, with each factor listed as many times as it appears in the factorization. The function iteratively divides the input number by the smallest divisor until it's no longer divisible, then increments the divisor and repeats the process until the number is reduced to 1. The test cases verify the correctness of the function for the inputs 8, 25, and 70.