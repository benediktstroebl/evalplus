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
    factors.append(n)
    return factors
```
The function `factorize` takes an integer `n` as input and returns a list of prime factors of `n` in the order from smallest to largest, together with the count of each factor in the product of all factors. 

The function uses a while loop to find all the factors of the number and a for loop to check the divisibility of each prime number up to the given number.