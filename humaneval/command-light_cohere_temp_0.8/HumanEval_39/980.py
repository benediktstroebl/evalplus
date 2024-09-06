```python
import math
def prime_fib(n):
    if n < 1:
        return n
    elif n == 1:
        return 1
    else:
        a, b = 2, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
            if math.is(gcd)(a, b):
                return b
        return b
```