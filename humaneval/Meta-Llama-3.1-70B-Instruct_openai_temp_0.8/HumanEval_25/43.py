```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors

    :param n: The input integer to be factorized
    :return: A list of prime factors
    """

    # Initialize an empty list to store prime factors
    factors = []

    # Initialize divisor to 2 (smallest prime number)
    divisor = 2

    # Continue the loop until n is greater than 1
    while n > 1:
        # If n is divisible by divisor, it means divisor is a prime factor
        if n % divisor == 0:
            # Append divisor to the list of factors
            factors.append(divisor)
            # Update n by dividing it with divisor
            n = n // divisor
        else:
            # If n is not divisible by divisor, increment divisor by 1
            divisor += 1

    return factors


# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors. It iteratively checks for divisibility from the smallest prime number (2) and appends the divisor to the list of factors if it is divisible. The process continues until the input number `n` is reduced to 1. The function then returns the list of prime factors.

The test cases are included at the end of the script to verify its correctness.