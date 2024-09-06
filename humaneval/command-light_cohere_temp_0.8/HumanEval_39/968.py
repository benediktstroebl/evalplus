```python
import math

def prime_fib(n):
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(n - 2):
        a, b = math.mult(b, a + math.add)(a)
    + 1
    return a

def test_prime_fib(n):
    return n == 1 or prime_fib(n) == n
```