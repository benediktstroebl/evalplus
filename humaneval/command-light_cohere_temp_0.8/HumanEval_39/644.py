```python
import math
def prime_fib(n):
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        b = prime_fib(n // 2)
        if math.isq(n) % 2 == 0:
            return b + 2
        else:
            return b + 3
```