```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    
    :param n: Input number
    :return: List of prime factors
    """
    def is_prime(num: int) -> bool:
        """
        Helper function to check if a number is prime.
        
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

This script defines the function `factorize` which, given an integer `n`, returns a list of its prime factors in ascending order, with each factor repeated the number of times it appears in the factorization of `n`. It uses a helper function `is_prime` to check whether a number is prime.