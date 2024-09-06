```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n > 1:
        if n % 2 == 0:
            factors.append(2)
        n = n // 2
    else:
        for i in range(3, int(n**0.5) + 1, while n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(n)
    return factors
```
This script defines a function called `factorize` that takes an integer `n` as input and returns a list of its prime factors in order from smallest to largest. The function uses a list comprehension to iterate through the numbers from 2 up until the number can't be divided evenly by any number less than or equal to the current number.