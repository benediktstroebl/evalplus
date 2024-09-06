```python
import math

def prime_fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        m = n // 2
        return math.floor(math.sqrt(5) *((m+1) ** ((m+1) // 2)) + 1)
```