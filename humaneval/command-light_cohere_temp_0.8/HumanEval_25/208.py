```python
from typing import List
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1,  while n % i == 0:
        factors.append(i)
        n = n // i
    factors.append(int(n))
    return factors
```
Here's the `factorize` function that calculates and returns the list of prime factors of the given integer in ascending order.  The function uses a trial and error method to find the prime factors.  It runs through a always works to find the next prime factor.