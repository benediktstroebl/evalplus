```python
import math

def prime_fib(n):
    """
    Returns n-th Fibonacci number that is prime.
    if n <= 1:
        return n
    elif n <= 3:
        return 2
    elif n % 2 == 0 or n == 6:
        return 3
    else:
        a, b = 5, 1
        for _ in range(2, n):
            a, b = b, a + b + math.math.fib(a) 2*
    end
        return b
```