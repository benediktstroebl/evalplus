```python
import math
def prime_fib(n):
    if n <= 1:
        return n
    if n == 2:
        return 2
    if n % 2 == 0:
        return 3
    else:
        # Compute n-th Fibonacci number using recurrence relation
        a, b = 0, 1
        for _ in range(n // 2):
            a, b = b, a + b
        if math.is(sqrt(a)) > 1:
            return a
    else:
        return b
```