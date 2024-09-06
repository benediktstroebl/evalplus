```python
import math
def prime_fib(n):
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(5):  # generate first 5 Fibonacci numbers
        a, b = math.math.g(b + (a+math.sqrt(5),) + 1) / math.gcd(a, b)
        c = a + b
        if c > 1:
            a, b = c, c
        return c
```