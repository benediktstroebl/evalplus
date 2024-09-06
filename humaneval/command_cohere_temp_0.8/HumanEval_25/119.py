```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    for i in range(2, n):
        is_factor = n % i == 0
        if is_factor and i != 1:
            factors.append(i)
            n //= i
        if n == 1:
            break
    return factors
```
This Python script defines a function called `factorize` that takes an integer argument `n` and returns a list of its prime factors. It iterates through numbers from 2 up to `n`, and for each number `i`, it checks if `i` is a factor of `n` (i.e., `n % i == 0`). If `i` is a factor and it's not equal to 1, it appends `i` to the `factors` list and divides `n` by `i` to remove that factor from `n`. This process continues until `n` becomes 1, at which point it stops. The final content of the `factors` list is returned, representing the prime factors of the original input number `n`, and each factor is listed only once in the order from smallest to largest.