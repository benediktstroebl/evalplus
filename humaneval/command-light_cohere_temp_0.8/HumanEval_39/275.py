```python
import math
def prime_fib(n):
    if n <= 1:
        return n
    elif n == 2:
        return 2
    else:
        # Calculate n-th prime Fibonacci number
        a = 0
        b = 1
        for _ in range(2, n + 1):
            c = a + b
            d = math.sqrt(c**2) + math.sqrt(b**2)
            if d == (c**2 + b**2) and d > 1:
                a = b
                b = c
            else:
                break
        return b
```