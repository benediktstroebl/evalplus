```python
import math
def prime_fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n <= 1:
        return n
    if n == 2:
        return 2
    factors = [1, 2]
    for i in range(3, n+1):
        for j in factors:
            if j > 1 and math.fib(i, j) == 1:
                factors.append(j)
    factors.
    for i in range(2, n//2+1):
        for j in factors:
            if j == i or j == i+1:
                continue
            else:
                return j
    return None
```