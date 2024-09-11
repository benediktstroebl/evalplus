```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    
    :param n: The number to be factorized
    :return: A list of prime factors
    """
    factors = []
    divisor = 2
    
    while n > 1:
        # If n is divisible by the divisor, add it to the list of factors and divide n
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        # If n is not divisible by the divisor, increment the divisor
        divisor += 1
    
    return factors


# Test the function
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```