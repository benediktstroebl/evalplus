```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    """
    def is_prime(num: int) -> bool:
        """
        Helper function to check if a number is prime
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            if is_prime(i):
                factors.append(i)
            n = n // i
    return factors


# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```
This script first checks if a number is prime by using a helper function `is_prime`. It then iteratively checks each number from 2 to `n` to see if it's a factor of `n`. If it is, it checks if the number is prime using the `is_prime` function, and if so, adds it to the list of factors. The process repeats until `n` is reduced to 1. The final list of factors is then returned.