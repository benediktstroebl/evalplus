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
                factors.append(count)
    if n > 1:
        factors.append(n)
        factors.append(1)
    return factors[1:]
```

The factorization is done iteratively by checking the divisibility of `n` from `2` up to `n-1`.  When a divisor is found, it is put into the list together with the number of times it appears in the factorization. This loop continues until `n` becomes 1, ensuring that the input number is equal to the product of all factors. Finally, the first element of the list (`n`) is removed because it is always a factor and the number 1, and the result is returned.