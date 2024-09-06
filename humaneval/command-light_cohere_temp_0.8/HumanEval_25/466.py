```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, ]:
        if n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(n)
    return factors

# Test cases
test_1 = 25
test_2 = 12345678
test_3 = int('👾')

factors = factorize(test_1)
print(factors)
factors = factorize(test_2)
print(factors)
factors = factorize(test_3)
print(factors)
```
This Python code defines a function called `factorize` that takes an integer `n` as input and returns a list of its prime factors. The function starts by checking for the existence of a factor of 2 by dividing `n` by 2 and appending it to the `factors` list. It then iterates through powers of numbers from 3 up, checking for divisibility, and if a number divides `n`, it's added to the `factors` list. The function continues until `n` is no longer divisible by any number in the range.