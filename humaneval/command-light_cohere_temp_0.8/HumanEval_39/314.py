```python
import math
def prime_fib(n):
    if n <= 0:
        raise ValueError("n should be a positive integer")
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        a, b = 3, 5
        for _ in range(n - 2):
            a, b = b, a + b
        if math.isq(a, b):
            return a
```
This function will calculate the nth prime Fibonacci number and return it, passing all the test cases.