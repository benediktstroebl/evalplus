```python
from typing import List
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1,):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors
```
The function factorizes the given number `n` by finding its prime factors. It starts by checking if `n` is even or odd, then it adds the number `2` to the `factors` list. It then iterates through odd numbers from 3 to the square root of `n`, while continuously dividing by the current number to check for divisibility. Finally, if `n` is greater than 2, the largest prime factor is the last number `n`.