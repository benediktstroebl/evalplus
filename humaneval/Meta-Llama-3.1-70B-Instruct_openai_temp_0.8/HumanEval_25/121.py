```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors.

    :param n: The number to factorize
    :return: A list of prime factors
    """
    def is_prime(num: int) -> bool:
        """
        Check if a number is prime.

        :param num: The number to check
        :return: True if the number is prime, False otherwise
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
        if n % divisor == 0 and is_prime(divisor):
            factors.append(divisor)
            n = n // divisor
        else:
            divisor += 1
    return factors


# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script uses a helper function `is_prime` to check if a number is prime. The main function `factorize` uses a while loop to find the prime factors of the input number `n`. It starts by checking if `n` is divisible by the current `divisor`, and if so, it adds the `divisor` to the list of factors and divides `n` by the `divisor`. If not, it increments the `divisor`. The loop continues until `n` is reduced to 1. The function returns the list of prime factors.