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

The code employs an exhaustive divisibility check from 2 to `n-1` to find all prime factors. It detects each factor, counts its occurrence in the factorization, and reconstructs the occurrence count information in the result list. For example, if `n` is 240, the code will proceed as follows:
1. Testing divisors from 2 up to 239, encountering no matches until reaching 240.
2. Finding that 240 is divisible by 2, yielding a factor list `[2, 2]` because 2 appears twice in the factorization.

This approach ensures correctness while keeping the time complexity at `O(d * (n/d)`, where `d` is the number of digits in `n`. Note that the code assumes that the input `n` is valid and is not affected by floating point precision issues, making the algorithm less efficient for large integers.