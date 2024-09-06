```python
from typing import List

def prime_factors(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    """
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(int(n))
    return factors

def factorize(n: int) -> List[int]:
    return [factor_frequency for factor_frequency in prime_factors(n)]
```
The `prime_factors` function returns all prime factors of a given integer `n` and `factorize` transposes this list into the required format. It considers integers 2 and 3 as prime. If you want to consider only numbers bigger than 2 as prime, you should change that in the function. 

You can test this code by calling the `factorize` function with various input numbers to verify the correctness of the solution. 
Please note that the handling of the prime designation is subjective, and the code can be adjusted to suit your requirements. P