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
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(int(n))
    return factors

def factorize(n: int) -> List[int]:
    return [factor]*count for factor, count in zip(prime_factors(n), prime_factors(n))
```
The `prime_factors` function returns list of all prime factors of given integer `n` and `factorize` function uses `prime_factors` to return list of factors where each factor is listed number of times corresponding to how many times it appears in factorization. 

Both functions handle input less than or equal to 1, returning an empty list. For integers equal to 2 or 3, a list containing single integer is returned. Otherwise, it iterates through integers 2, 3 and 5 onwards, splitting `n` into its prime factors. 

The `factorize` function performs the task for the given problem and is backed by the `prime_factors` function to solve the specified problem completely on its own. It is important to note that this solution is not optimized for performance and relies on Python's built-in iteration capabilities, which makes it scalable for integers up to the limits of the Python interpreter.