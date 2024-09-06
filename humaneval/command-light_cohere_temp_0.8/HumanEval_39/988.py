```python
import math
def prime_fib(n):
    if n == 0 or n == 1:
        return n
    else:
        # base case
        a, b = 2, 3
        for _ in range(2, n + 1):
            if math.isq(a, b) > 1:
                a, b = b, a + b
            else:
                break
        return b
```