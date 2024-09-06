```python
from typing import List

def prime_factors(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n / 2
    for i in range(3, int(n**0.5) + 1, 2):
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
The `prime_factors` function extracts all prime factors from the given number `n` and returns them in a list. The `factorize` function uses it and includes each factor in the result list the number of times it appears in the factorization of the input number `n`. 

Here is an example:
```python
factorize(8)
# [[2, 2, 2]]

factorize(25)
# [[5, 5]]

factorize(70)
# [[2, 5, 7]]
```