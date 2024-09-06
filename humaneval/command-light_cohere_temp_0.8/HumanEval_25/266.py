```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    for num in range(int(n**0.5) + 2, while n %= num == 0:
        factors.append(num)
    return factors
```
The function `factorize()` takes an integer `n` as input and returns a list of its prime factors. The function first checks for the factor of 2 and appends it to the list. Then, it uses the factor of i to continue the process until the next prime number is found.