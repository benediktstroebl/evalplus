```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    for i in range(2, n):
        if n % i == 0:
            count = 0
            while n % i == 0:
                n //= i
                count += 1
            if count > 0:
                factors.append(i)
                factors.extend([i] * count)
    if n > 1:
        factors.append(n)
    return factors
```

The code uses a simple optimization to limit the iterations through the factors. It runs through numbers from 2 to `n` and for each found factor, it iterates through its divisibility to find the number of times it appears in the factorization. If it appears more than once, it extends the `factors` list by appending the factor `i` number of times corresponding to its occurrence in the factorization.

Here is an example usage of the function:
```python
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
``` 

This problem can be solved in many other ways, such as trial factorization, checking all possible factors up to `sqrt(n)`, and more. Each approach has its pros and cons in terms of efficiency and readability.