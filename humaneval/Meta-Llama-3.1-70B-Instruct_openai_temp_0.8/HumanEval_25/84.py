```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    """
    factors = []
    divisor = 2
    while n > 1:
        # if n is divisible by divisor, add divisor to factors and divide n by divisor
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        # increment divisor by 1
        divisor += 1
    return factors

# test cases
print(factorize(8))     # [2, 2, 2]
print(factorize(25))    # [5, 5]
print(factorize(70))    # [2, 5, 7]
print(factorize(100))   # [2, 2, 5, 5]
print(factorize(1024))  # [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
```