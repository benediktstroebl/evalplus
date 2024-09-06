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
The factorization algorithm is a simple trial division technique. The code starts by iterating through numbers from 2 up to `n` to find the smallest prime factor. When a number `i` is found such that `n % i == 0`, the algorithm counts how many times `i` appears as a factor by repeatedly dividing `n` by `i` while updating the count. After finding all factors, the code removes the count tuple from the list and returns the list of factors and counts. This algorithm has a time complexity of `O(sqrt(n))` since it only needs to check factors up to the square root of `n`.