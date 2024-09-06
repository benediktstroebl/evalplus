```python
import math

def prime_fib(n):
    if n == 0 or n == 1:
        return n
    a, b = 2, 3
    for _ in range(2, n):
        a, b = math.mult(a, b) + 1, b
    return a

# Test
test_result = prime_fib(10)
print(test_result)
```