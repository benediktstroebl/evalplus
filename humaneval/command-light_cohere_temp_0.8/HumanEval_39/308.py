```python
import math
def prime_fib(n):
    """
    Return n-th Fibonacci number and check if it's prime.
    if n <= 1:
        return n
    if n % 2 == 0 or n % 3 == 0:
        return False
    sqrt_n = int(math.sqrt(n))
    if sqrt_n * sqrt_n <= n:
        for i in range(5):
            if n % (i + 1) == 0:
                return False
    return n
```