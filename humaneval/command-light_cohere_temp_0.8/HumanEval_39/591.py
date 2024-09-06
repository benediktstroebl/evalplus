```python
import math
def prime_fib(n):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 2
    mid = math.floor(math.sqrt(math.pow(2,n / 2)) + 1
    if n >= mid:
        return prime_fib(mid)
    return mid + 1
```