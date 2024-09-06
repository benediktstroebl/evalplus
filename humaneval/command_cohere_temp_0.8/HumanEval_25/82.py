```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    for i in range(2, n):
        is_factor = n % i == 0
        if is_factor and i != 1:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors
```

The factorization process is iterative and involves checking for divisibility by numbers starting from `2` up to the input number `n`. When a divisor is found, it is added to the `factors` list and the input number is updated by dividing by the current divisor. The process continues until the input number becomes 1, at which point any remaining factors are added to the list. This ensures that the list of prime factors contains all divisors of the input number in the desired order, with each factor listed the number of times it appears in the factorization.