```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    for i in range(2, n):
        is_factor = n % i == 0
        if is_factor and i != 1:
            factors.append(i)
            while is_factor:
                n //= i
                is_factor = n % i == 0
            if n == 1:
                break
    if n > 1:
        factors.append(n)
    return factors
```

The factorization is done iteratively by checking if the number is divisible by each number from 2 to `n`. 
For each divisor found, it appends it to the list of factors and divides the number accordingly.

This solution has a time complexity of O(sqrt(n)) since it only iterates up to the square root of `n`. After that, it iterates over each divisor which brings the total time complexity to O(n sqrt(n)).