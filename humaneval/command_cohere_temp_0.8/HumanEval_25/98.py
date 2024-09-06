```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    for i in range(2, n):
        is_factor = n % i == 0
        if is_factor and i != 1:
            factors.append(i)
            while is_factor:
                n //= i
                is_factor = n % i == 0
            if n == 1:
                break
    return factors
```

This Python script defines a function called `factorize`, which takes in an integer `n` as input and returns a list of its prime factors. The function starts by creating an empty list called `factors` to store the prime factors. It then iterates through numbers from 2 up to `n` (inclusive) to identify potential factors. For each number `i`, it checks if `i` is a factor of `n` by performing the modulo operation (`n % i`). If `i` is a factor and it's not equal to 1, it adds `i` to the `factors` list and initiates a loop to further factorize `n` by dividing it by `i` until `i` is no longer a factor. The loop ensures that each prime factor is listed the number of times it appears in the factorization process. Once the factorization is complete, the function returns the `factors` list.