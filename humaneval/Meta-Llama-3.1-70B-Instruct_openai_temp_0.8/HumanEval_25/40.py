```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    :param n: Input integer to be factorized
    :return: List of prime factors
    """
    def is_prime(num: int) -> bool:
        """
        Helper function to check if a number is prime
        :param num: Number to be checked
        :return: True if the number is prime, False otherwise
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    factors = []
    divisor = 2
    while n > 1:
        # Find the smallest prime factor
        while not is_prime(divisor):
            divisor += 1
        # Divide the number by the factor until it's no longer divisible
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        # Move on to the next potential factor
        divisor += 1
    return factors

# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors. The function uses a helper function `is_prime` to check if a number is prime. It iteratively finds the smallest prime factor of the input number, divides the number by this factor until it's no longer divisible, and repeats the process until the number is reduced to 1. The prime factors are stored in a list and returned as the result.

The script also includes test cases to demonstrate its correctness.