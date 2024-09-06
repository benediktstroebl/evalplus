```python
import math
def prime_fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1:
        return 1
    else:
        a, b = 2, 3
        for _ in range(n - 2):
            a, b = math.math(b + afib(a) + 1, a)
        return b
```