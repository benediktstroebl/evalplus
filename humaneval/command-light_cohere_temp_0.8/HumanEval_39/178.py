```python
import math
def prime_fib(n):
    if n <= 0:
        raise ValueError("n should be a positive integer")
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a, b = 3, 2
        for _ in range(2, n):
            a, b = b, a + b
        if math.isqueen(a) and math.isqueen(b):
            return a
```
This function takes an integer n as input and returns the n-th Fibonacci number that is prime.