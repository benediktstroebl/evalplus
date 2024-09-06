```python
import math
def prime_fib(n):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    result = 5
    while True:
        if math.gcd(result, n) == 1:
            break
        result += 1
    return result
```