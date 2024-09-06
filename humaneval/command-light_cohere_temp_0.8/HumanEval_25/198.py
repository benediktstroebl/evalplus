```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    while n > 1:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                factors.append(i)
                n = n // i
    factors.append(n)
    return factors
```
This function will return a list of prime factors of the given number in order from smallest to largest. This is a desired result for the markdown code block.