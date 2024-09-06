```python
import math
def prime_fib(n):
    if n <= 1:
        return n
    if n % 2 == 0:
        return math.floor(math.sqrt(5 *n) / 2)
    else:
        m = 2
        for i in range(3, n + 2, 2):
            m = int(math.sqrt(m * (m + 1)) + 1)
        return m
```