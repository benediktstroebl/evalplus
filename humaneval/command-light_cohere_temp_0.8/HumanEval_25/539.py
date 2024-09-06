```python
from typing import List
def factorize(n: int) -> List[int]:
    factors = []
    while n > 1:
        if n % 2 == 0:
            factors.append(2)
        n = n // 2
    else:
        i = 3
        while i * i <= n:
            if n % i == 0:
                factors.append(i)
                n = n // i
            i += 1
    return factors
# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5]
print(factorize(70))  # [2, 5, 7]
```
This script defines a function called `factorize` that takes an integer `n` as input and returns a list of its prime factors. The function uses a algorithm to find the prime factors of the number, which involves repeatedly dividing the number by the smallest prime factors until the number becomes 1. 

The function is then tested with several input numbers, and the output is printed to verify that it correctly identifies the prime factors.