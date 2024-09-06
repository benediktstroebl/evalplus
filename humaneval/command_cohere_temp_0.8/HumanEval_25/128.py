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

The factorization process is done iteratively by checking the divisibility of `n` from `2` up to `n-1`.  If a divisor is found, the number is divided by that divisor several times, updating a count of how many times it divides the number. Once the while loop exits, the divisor is added to the list with its counting the number of times it appeared in the factorization. This process is repeated for all divisers up to the square root of the number, and if the remaining number is more than 1 it is appended to the list with its count set to 1.