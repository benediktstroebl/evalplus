```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors

    :param n: The integer to factorize
    :return: List of prime factors
    """
    def is_prime(num: int) -> bool:
        """Check if a number is prime"""
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
        elif is_prime(divisor) and divisor * divisor > n:
            factors.append(n)
            break
        else:
            divisor += 1
    return factors


# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors. It uses a helper function `is_prime` to check if a number is prime.

The `factorize` function starts by dividing the input number `n` by the smallest prime number, which is 2. It continues to divide `n` by the smallest divisor until `n` is no longer divisible by that divisor. It then increments the divisor until it finds the next number that can divide `n`, which will necessarily be a prime number.

The process continues until `n` has been reduced to 1, at which point all of its prime factors have been found. The prime factors are stored in a list and returned by the function.

The test cases at the end of the script demonstrate how the `factorize` function can be used to find the prime factors of different numbers.