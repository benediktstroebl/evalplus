```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The input number to be factorized.

    Returns:
        List[int]: A list of prime factors.
    """
    def is_prime(num: int) -> bool:
        """
        Helper function to check if a number is prime.

        Args:
            num (int): The number to check.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def prime_factors(num: int) -> List[int]:
        """
        Helper function to generate prime factors.

        Args:
            num (int): The number to generate prime factors for.

        Returns:
            List[int]: A list of prime factors.
        """
        factors = []
        for i in range(2, num + 1):
            if is_prime(i):
                while num % i == 0:
                    factors.append(i)
                    num //= i
        return factors

    return prime_factors(n)


# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors. The function uses two helper functions, `is_prime` and `prime_factors`, to check if a number is prime and to generate the prime factors, respectively.

The `is_prime` function checks if a number is prime by iterating from 2 to the square root of the number and checking for divisibility.

The `prime_factors` function generates the prime factors by iterating from 2 to the input number and checking if each number is prime. If a number is prime, it is divided out of the input number as many times as possible, and the prime factor is added to the list.

Finally, the `factorize` function calls `prime_factors` to generate the list of prime factors and returns it.

The test cases at the end of the script demonstrate the function's correctness.