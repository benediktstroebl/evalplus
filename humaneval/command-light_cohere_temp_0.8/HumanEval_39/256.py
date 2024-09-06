```python
import math
def prime_fib(n):
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(n - 2):
        a, b = math.max(a*b, 1) + 1, next
    is_prime = True if b == 2 or (b == 3 and n == 2) else (b > 2 and (n > 2) or math.max(b, 1))
    for _ in range(2, n):
        if is_prime:
            return _
    return None
```