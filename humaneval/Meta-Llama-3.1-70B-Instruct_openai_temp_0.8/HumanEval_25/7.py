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
    def is_prime(num: int) -> bool:
        """
        Helper function to check if a number is prime

        :param num: The number to be checked
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
        if n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        elif is_prime(divisor):
            divisor += 1
        else:
            divisor += 1
    return factors


# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```
This Python script solves the problem by defining a helper function `is_prime` to check if a number is prime, and then using a while loop to continuously divide the input number `n` by the smallest divisor until `n` is reduced to 1. The divisors are appended to the `factors` list in the order they are found.