```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5 / 2, step by step):
        while n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(n)
    return factors
```
This function takes an integer n as input and returns a list of its prime factors in descending order. It uses a iterative approach to find the prime factors, starting with 2 and then checking for divisibility with numbers increasing up to the square root of the number. The function runs in O(n) time.