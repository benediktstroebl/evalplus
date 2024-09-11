```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    
    :param n: integer to factorize
    :return: list of prime factors
    """
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
This script defines a function `factorize` which takes an integer as input and returns a list of its prime factors. The function iterates over all numbers from 2 to the square root of the input number, checks if the current number is a factor, and if it is, divides the input number by the factor and adds the factor to the list. Finally, if the remaining number is greater than 1, it is added to the list as the last factor.