```python
import math
def prime_fib(n):
    if n <= 1:
        return n
    if n == 2:
        return 2
    if n % 2 == 0:
        return 3
    i = 5
    while i * i <= n:
        if math.gcd(i, n) == 1:
            j = i + 2
            if j > n:
                break
            if n % j == 0:
                return j
    return n
```