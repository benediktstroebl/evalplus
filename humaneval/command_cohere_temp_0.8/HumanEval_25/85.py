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
                else:
                    break
    if n > 1:
        factors.append(n)
    return factors
```

The factorization is done iteratively by checking the divisibility of `n` from `2` up to `n-1`.  When a number is found to be a factor, it is appended to the factors list and the value of `n` is divided by the current factor, iterating through the process with the new factor as many times as needed. The final factor left, when all others have been removed, is appended to the list as well. This ensures the list of factors contains each prime factor the desired number has, and that each factor appears the number of times it's needed to render `n`.