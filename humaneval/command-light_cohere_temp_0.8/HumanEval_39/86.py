```python
import math
def prime_fib(n):
    if n <= 1:
        return n
    elif n == 2:
        return 2
    else:
        a, b = 3, 2
        for _ in range(n - 2):
            a, b = math.isprime(a + b), next_)
        return a
```