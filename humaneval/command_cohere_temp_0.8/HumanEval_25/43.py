```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    for i in range(2, n):
        if n % i == 0:
            count = 0
            while n % i == 0:
                n //= i
                count += 1
            if count > 0:
                factors.append(i)
                factors.append(count)
    if n > 1:
        factors.append(n)
        factors.append(1)
    return factors[1:]
```
The factorize function iterates through numbers from 2 up to the given integer `n` and checks if it's a divisor of `n` (i.e., `n % i == 0`). If it is, the respective number is appended to the `factors` list, and a count of how many times it appears in the factorization is added to the list. This step is repeated while the number i is a divisor of n. After that, if there is a remaining factor `n` greater than 1, it is appended to the list along with a count of 1 since it appears once in the factorization. The final list of factors is returned after discarding the initial count value.