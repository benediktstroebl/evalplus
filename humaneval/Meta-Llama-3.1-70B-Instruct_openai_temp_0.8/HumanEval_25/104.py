```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    :param n: Input integer
    :return: List of prime factors
    """
    def is_prime(x: int) -> bool:
        """
        Helper function to check if a number is prime.
        :param x: Number to check
        :return: True if prime, False otherwise
        """
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    factors = []
    i = 2
    while n > 1:
        if n % i == 0 and is_prime(i):
            factors.append(i)
            n //= i
        else:
            i += 1
    return factors


# Test cases
assert factorize(8) == [2, 2, 2]
assert factorize(25) == [5, 5]
assert factorize(70) == [2, 5, 7]
```

This script defines a function `factorize` that takes an integer `n` and returns a list of its prime factors in the order from smallest to largest. It uses a helper function `is_prime` to check if a number is prime.

The `factorize` function works by dividing the input number `n` by the smallest prime number (which is 2) as long as it's divisible. Then it increments the divisor until it finds the next number that can divide `n`, which will necessarily be a prime number. This process continues until `n` is reduced to 1.

The test cases at the end of the script verify that the function works correctly for the inputs 8, 25, and 70.