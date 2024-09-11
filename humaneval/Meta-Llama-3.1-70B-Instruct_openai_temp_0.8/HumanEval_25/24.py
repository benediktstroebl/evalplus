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
        Helper function to check if a number is prime
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
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors. The function uses a helper function `is_prime` to check if a number is prime, but it is not actually used in the main function. The main function iterates over numbers from 2 to the square root of `n`, and if `n` is divisible by the current number, it divides `n` by the current number and adds it to the list of factors. If `n` is greater than 1 at the end, it means that `n` is a prime number and it is added to the list of factors. The function returns the list of factors.