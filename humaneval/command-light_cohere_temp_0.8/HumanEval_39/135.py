```python
import math
def prime_fib(n):
    if n <= 1:
        return n
    if n <= 3:
        return 2
    m = math.sqrt(5)
    limit = int(math.log(m, n / 2))
    for i in range(limit + 1):
        if math.gcd(i, m) == 1:
            temp = i
            i = m
            m = temp
    return i
```