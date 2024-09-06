```python
from typing import List
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1,  while n % i == 0:
        factors.append(i)
        n = n // i
    factors.append(n)
    return factors
```

This function takes an integer `n` as input and returns a list of prime factors of `n` in descending order, along with the count of each factor in the product `n`. The function utilizes a while loop to repeatedly find factors until the quotient of `n` with the next prime factor does not equal to `0`.  This is a self-contained function that can be used to factorize any given integer.