```python
import math
def prime_fib(n):
    if n <= 1:
        return n
    if n == 2:
        return 2
    if n % 2 == 0:
        return 3
    prime = math.sqrt(math.sqrt(n) + 1) + 1
    for i in range(5, prime, 2):
        if n % i == 0:
            return i
```