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
    return factors

# Test case 1
print(factorize(8))

# Test case 2
print(factorize(25))

# Testcase3
print(factorize(70))
```

This script defines a function called `factorize` that takes an integer `n` as input and returns a list of its prime factors. The function first checks for the factorization by dividing `n` by 2 and appending the number 2 to the list of factors. It then iterates through powers of numbers from 3 to the square root of `n` until it finds the first factor that doesn't divide `n` evenly.