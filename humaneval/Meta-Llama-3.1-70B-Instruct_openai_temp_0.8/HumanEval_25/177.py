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
This script defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors in ascending order. The function uses a simple trial division approach to find the prime factors. It starts with the smallest prime number (2) and checks if it divides `n`. If it does, it divides `n` by this factor and adds it to the list of factors. This process is repeated until `n` is reduced to 1. If `n` is still greater than 1 at the end, it means that `n` itself is a prime number, so it is added to the list of factors. The function returns this list of factors.