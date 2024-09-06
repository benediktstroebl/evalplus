```python
from typing import List
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n //= i
    return factors
```
This function accepts an integer `n` as input and returns a list of its prime factors. The function utilizes a process where it iterates through the numbers 2, 3, ... until the square root of the number, continuously adding factors to the list until they are no multiples of the current number.