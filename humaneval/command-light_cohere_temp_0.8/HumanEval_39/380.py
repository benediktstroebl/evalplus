```python
import math

def prime_fib(n):
    if n <= 1:
        return n
    if n <= 3:
        return 2
    a, b = 3, 5
    for _ in range(4, n + 1):
        a, b = math.next_prime(math.gcd(a, b))
    return a
```