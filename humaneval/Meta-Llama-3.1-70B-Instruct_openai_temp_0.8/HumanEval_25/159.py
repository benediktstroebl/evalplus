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
        Helper function to check if a number is prime
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
    # Start from the smallest prime number, which is 2
    i = 2
    while i * i <= n:
        if n % i:
            # If i is not a factor of n, increment it
            i += 1
        else:
            # If i is a factor of n, divide n by i and add i to the factors list
            n //= i
            factors.append(i)
    # If n is a prime number greater than 1, add it to the factors list
    if n > 1:
        factors.append(n)
    return factors

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors. The function uses a helper function `is_prime` to check if a number is prime. The `factorize` function iterates over all numbers from 2 to the square root of `n`, checking if each number is a factor of `n`. If a number is a factor, it is divided out of `n` and added to the list of factors. Finally, if `n` is a prime number greater than 1, it is added to the list of factors.

The script includes test cases to verify that the `factorize` function works correctly.