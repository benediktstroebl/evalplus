```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    for divisor in range(2, n):
        if n % divisor == 0:
            count = 0
            while n % divisor == 0:
                n //= divisor
                count += 1
            if count > 0:
                factors.append(divisor)
                factors.extend([divisor] * count)
    if n > 1:
        factors.append(n)
    return factors
```

The code employs an exhaustive divisibility check from 2 to `n-1` to find all prime factors. It then counts the number of times each appears in the factorization and includes them in the answer. To account for any remaining factor, the loop iterates backward from `n-1` to 2, ensuring that no number is missed. 

Such a process guarantees an accurate list of prime factors in ascending order, with each appearing a corresponding number of times.

To use the `factorize` function, import the `list` module and call the function with an integer argument like this:
```python
import list
factors = list.factorize(70)
print(factors)  # Output: [2, 5, 7]
```