```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    """
    def prime_factors(num: int) -> List[int]:
        i = 2
        factors = []
        while num > 1:
            if num % i == 0:
                factors.append(i)
                num //= i
            else:
                i += 1
        return factors

    return prime_factors(n)


# Example usage:
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a helper function `prime_factors` inside the main function `factorize`, to calculate the prime factors of the input number `n`. The helper function iterates from 2 up to `n`, appending each factor it finds to the result list and dividing `n` by that factor until `n` is reduced to 1. This way, it guarantees that each prime factor appears in the result list the correct number of times.