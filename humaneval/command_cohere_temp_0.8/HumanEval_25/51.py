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

The factorization is done iteratively by dividing the number n by factors from 2 up to n itself. Whenever a factor is found to be divisior of n, its presence is noted and number n is divided by it. The process is repeated until n becomes 1. Note that this method is not the most efficient one to factorize a number, but it works for all positive integers. 

Such iterative approach is done so that we can easily extend the method to factorize large numbers, even though efficient algebraic methods are available for factoring small numbers. 

The function returns the list of prime factors in the order from smallest to largest. Each of the factors is listed corresponding to how many times it appears in factorization.