```python
import math

def prime_fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a, b = 1, 2
        for _ in range(n - 2):
            a, b = b, a + b
        if math.is(sqrt(a)) > 1:
            return a
```

This function computes the n-th Fibonacci number that is prime, using an iterative approach. It also includes input validation to ensure the input is a positive integer.