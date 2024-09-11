```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    :param n: The number to factorize
    :return: A list of prime factors
    """
    def is_prime(num: int) -> bool:
        """
        Check if a number is prime

        :param num: The number to check
        :return: True if the number is prime, False otherwise
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    factors = []
    for i in range(2, n + 1):
        if is_prime(i):
            while n % i == 0:
                factors.append(i)
                n //= i
    return factors

# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```
This script defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors. It uses a helper function `is_prime` to check if a number is prime. The `factorize` function iterates over all numbers from 2 to `n` and checks if they are prime. If a prime number is found, it is divided into `n` as many times as possible and added to the list of factors. The process continues until `n` is reduced to 1. The script also includes test cases to verify the correctness of the `factorize` function.