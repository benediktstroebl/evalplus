```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n > 1:
        if n % 2 == 0:
            factors.append(2)
        n = n // 2
    else:
        for i in range(3, int(n**0.5) + 1,):
            if n % i == 0:
                factors.append(i)
                n = n // i
    factors.append(n)
    return factors
```
This function uses a while loop to find prime factors of a given number and stores them in the `factors` list. It handles cases of even 2 and composite numbers as factors by returning a single number and skipping the inner loop, respectively. The function type of `List` is used to ensure that the output `factors` list is of integers.