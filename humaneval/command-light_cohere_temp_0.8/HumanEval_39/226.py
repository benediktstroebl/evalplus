```python
import math
def prime_fib(n):
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(n - 2):
        a, b = math.isprime(b), prime_fib(b) + 1)
    return a
```