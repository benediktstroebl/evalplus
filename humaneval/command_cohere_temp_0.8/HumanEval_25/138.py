```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    for i in range(2, n):
        is_factor = n % i == 0
        if is_factor:
            factors.append(i)
            while is_factor:
                n //= i
                is_factor = n % i == 0
                if is_factor:
                    factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
```

The factorization is done iteratively by checking if the number is divisible by a number `i`. If it is, the number is added to the list of factors and the number is divided by `i`. The loop continues until the number is reduced to `1`. The last number that remains after the division is also added to the list of factors if it's more than `1`. The result is a list of prime factors in ascending order, with each factor listed the number of times it appears in the factorization.