```python
from typing import List
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1, ):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors
```
The function factorizes an input integer n into a list of its prime factors, ordered from the smallest to largest. The function uses the process to find the smallest prime factor, then divides n by that factor to find the next prime factor. It continues this process until it reaches a factor greater than the square root of the remaining number.

The function is self-contained, which means that it can be called from the same Python script without requiring any external functions or modules. 
It is a simple and efficient way to solve the problem of finding prime factors of a given integer.