```python
import math

def prime_fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 2
    if n == 2:
        return 3
    x, y = 3, 4
    for _ in range(n - 2):
        x, y = x + y, x % math.make_prime(x)
    return x
```

This function calculates the n-th Fibonacci number that is prime using the math module's `make_prime` function. The function is self-contained and does not rely on any external imports.