```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors

    :param n: Input integer
    :return: List of prime factors
    """
    def is_prime(num: int) -> bool:
        """
        Helper function to check if number is prime
        :param num: Number to check
        :return: True if number is prime, False otherwise
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


# Test cases
print(factorize(8))    # Expected output: [2, 2, 2]
print(factorize(25))   # Expected output: [5, 5]
print(factorize(70))   # Expected output: [2, 5, 7]
```

This script defines a function `factorize` that calculates the prime factors of a given integer. The function uses a helper function `is_prime` to check if a number is prime, but in this case, it's not actually used because we're iterating through all numbers and checking divisibility directly. If the input number `n` is divisible by the current number `i`, we divide `n` by `i` and append `i` to the list of factors. We repeat this process until `n` is reduced to 1. If `n` is greater than 1 at the end, it means that `n` itself is a prime factor, so we append it to the list. The function returns the list of prime factors.