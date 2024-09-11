```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    
    :param n: The number to be factorized
    :return: A list of prime factors
    """
    factors = []
    divisor = 2
    while n > 1:
        # If n is divisible by the current divisor, add it to the list of factors and divide n by the divisor
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        # If the current divisor is 2, increment it by 1. Otherwise, increment it by 2 to skip even numbers.
        divisor = 3 if divisor == 2 else divisor + 2
    return factors

# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize(n)` that takes an integer `n` as input and returns a list of its prime factors in the order from smallest to largest. Each factor is listed the number of times it appears in the factorization.

The function uses a simple iterative approach to find the prime factors. It starts by checking divisibility by the smallest prime number (2) and then increments the divisor by 1 or 2 to skip even numbers. This approach ensures that the factors are found in ascending order.

The test cases at the end of the script demonstrate the function's correctness by comparing its output to the expected output for different inputs.