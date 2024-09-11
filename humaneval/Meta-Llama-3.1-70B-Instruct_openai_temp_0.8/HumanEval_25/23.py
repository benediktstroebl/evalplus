```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    
    :param n: The input integer
    :return: List of prime factors
    """
    def is_prime(num: int) -> bool:
        """
        Helper function to check if a number is prime
        :param num: The input number
        :return: True if the number is prime, False otherwise
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    factors = []
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            factors.append(i)
            n //= i
            while n % i == 0:
                factors.append(i)
                n //= i
    return factors

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```
This script defines the `factorize` function that takes an integer `n` and returns a list of its prime factors. The function uses a helper function `is_prime` to check if a number is prime. The `factorize` function iterates over numbers from 2 to `n`, checks if the current number is a factor of `n` and if it's prime, and if so, adds it to the list of factors and divides `n` by this factor. The process is repeated until `n` is reduced to 1. The test cases demonstrate the usage of the `factorize` function.