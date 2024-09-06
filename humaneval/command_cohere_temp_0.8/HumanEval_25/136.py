```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    for divisor in range(2, n):
        if n % divisor == 0:
            count = 0
            while n % divisor == 0:
                n //= divisor
                count += 1
            if count > 0:
                factors.append(divisor)
                factors.extend([divisor] * count)
    if n > 1:
        factors.append(n)
    return factors
```

The factorization process is done iteratively, checking the divisibility of the number `n` by integers ranging from 2 to `n` itself. When a divisor is found, the code uses an iterative approach to divide `n` by the divisor as many times as possible. To ensure that each divisor is listed only once in the final result, the code appends the divisor to the `factors` list, and extends it with a list of the same divisor as many times as its occurrence. The resulting list is then returned as the output.