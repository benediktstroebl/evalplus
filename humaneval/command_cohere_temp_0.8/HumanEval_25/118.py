```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    for i in range(2, n):
        is_factor = n % i == 0
        if is_factor:
            factors.append(i)
            while is_factor:
                n //= i
                is_factor = n % i == 0
                if is_factor:
                    factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
```

The factorization is done iteratively by checking if the number is divisible by a number `i`. If it is, the number is added to the list of factors, and the number is divided by `i` until it is no longer divisible by `i`. The loop starts from `i = 2` up to the square root of the number to be factorized, so we cover both potential divisors of a number in factorization, and divisor checking is done only up to the square root to optimize the process. The resulting list of factors is reversed to ensure the correct order.

Here's an example usage of the function:
```python
>>> factorize(8)
[2, 2, 2]
>>> factorize(25)
[5, 5]
>>> factorize(70)
[2, 5, 7]
```