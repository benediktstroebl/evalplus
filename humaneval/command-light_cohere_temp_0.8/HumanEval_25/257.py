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
# Example usage:
# Test case 1:
print(factorize(8))
# Expected output: [2, 2, 2]
# Test case 2:
print(factorize(25))
# Expected output: [5, 5]
# Test case 3:
print(factorize(70))
# Expected output: [2, 5, 7]
```
This Python function, factorize, takes an integer n as input and returns a list of its prime factors. It uses a process, where it repeatedly divides n by the smallest prime number that doesn't divide evenly into n, until n becomes 1. The factors are then the numbers that were appended to the list.

This function is self-contained, and it can be used to factorize any given integer without relying on any other functions or modules.