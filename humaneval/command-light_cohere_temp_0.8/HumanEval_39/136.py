```python
import math

def prime_fib(n):
    """
    Returns n-th Fibonacci number and checks if it's prime.
    if n <= 1:
        return n
    elif n % 2 == 0:
        return prime_fib(n - 2)
    else:
        return prime_fib(math.sqrt(5)) + prime_fib(math.sqrt(5))
```