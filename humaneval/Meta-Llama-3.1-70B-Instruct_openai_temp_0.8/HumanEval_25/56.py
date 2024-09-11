```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors

    :param n: Input integer to be factorized
    :return: List of prime factors in the order from smallest to largest
    """
    def is_prime(num: int) -> bool:
        """
        Helper function to check if a number is prime

        :param num: Number to be checked
        :return: True if number is prime, False otherwise
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    factors = []
    divisor = 2
    while n > 1:
        # If n is divisible by divisor, add it to the factors list and divide n
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        # If divisor is not a factor, increment it and check again
        divisor += 1
        # If divisor is not prime, increment it until we find a prime number
        while not is_prime(divisor):
            divisor += 1
    return factors


# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a `factorize` function that takes an integer `n` and returns a list of its prime factors. It uses a helper function `is_prime` to check if a number is prime. The `factorize` function works by dividing the input number `n` by the smallest prime divisor (starting from 2) until it is no longer divisible. The divisor is then incremented and the process repeats until `n` is reduced to 1. The list of divisors is returned as the result.

The test cases at the end of the script demonstrate the function's correctness.