```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    for i in range(2, n):
        is_factor = n % i == 0
        if is_factor:
            factors.append(i)
            while is_factor:
                n //= i
                is_factor = n % i == 0
                if is_factor:
                    factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
```

The factorize function takes an integer n as input and returns a list of its prime factors. It starts by iterating from 2 up to n-1. It checks if the current number is a factor of n, if it is, the loop accumulates all the factors and divides n by the current factor. The process continues until n becomes 1. The final factor left is n, since it's the only number that can't be divided by any other number- hence the smallest number that can't be divided by anything else. 

Here is a example usage of the function for the provided tests:
```python
>>> factorize(8)
[2, 2, 2]
>>> factorize(25)
[5, 5]
>>> factorize(70)
[2, 5, 7]
```