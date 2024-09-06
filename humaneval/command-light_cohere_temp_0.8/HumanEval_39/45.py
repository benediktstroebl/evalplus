```python
import math
def prime_fib(n):
    if n <= 0:
        raise ValueError("Input n must be a positive integer.")
    if n <= 1:
        return n
    if n == 2:
        return 2
    result = 2
    for i in range(2, n):
        if math.isprime(result + i):
            result = result + i
    return result
```