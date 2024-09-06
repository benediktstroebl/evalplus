```python
import math
def prime_fib(n):
    if n <= 1:
        return n
    else:
        if math.sqrt(n) <= 2:
            return math.floor(n * (2 * (n - 1) ** 0.5))
        if n % 2 == 0:
            return math.floor(n** 0)
        else:
            return math.floor((n - 1 + math.floor(n / 2))
```