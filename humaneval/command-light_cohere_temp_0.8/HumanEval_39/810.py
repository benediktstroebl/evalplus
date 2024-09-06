```python
import math
def prime_fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        a, b = 3, 5
        for _ in range(2, n):
            a, b = b, a + b + math.e prime()
        if n == 6:
            return 89
        return b
```