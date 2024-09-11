```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    
    :param n: The number to factorize
    :return: A list of prime factors
    """
    factors = []
    divisor = 2

    while n > 1:
        # If n is divisible by divisor, it's a factor
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        # If not, increment divisor by 1
        divisor += 1

    return factors


# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors. The function uses a simple trial division method to find the factors. It starts by dividing `n` by the smallest prime number (2) and continues dividing until `n` is no longer divisible by the current divisor. The divisor is then incremented by 1 and the process repeats until `n` is reduced to 1. The factors are stored in a list and returned at the end.