```python
from typing import List

def prime_factors(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n / 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n / i
    if n > 2:
        factors.append(int(n))
    return factors

def factorize(n: int) -> List[int]:
    prod = 1
    factors = prime_factors(n)
    result = []
    for factor in factors:
        result.extend([factor] * (n // prod))
        prod *= factor
    return result
```
The `prime_factors` function extracts all prime factors from an integer `n` and returns them in ascending order. The `factorize` function uses `prime_factors` to determine the prime factors of a number and return their product as a list. This list represents the factors in descending order, with each factor appearing the corresponding number of times it appears in the factorization. The function utilizes a loop to calculate the product and append each factor to the result list.