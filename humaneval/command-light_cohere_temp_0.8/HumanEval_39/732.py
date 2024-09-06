```python
import math

def prime_fib(n):
    """
    returns n-th Fibonacci number that is also prime
    """
    if n == 1:
        return 2
    if n <= 1 or n % 2 == 0:
        return False
    i = 2
    while i * i <= n:
        if math.isum(i, n) == 0:
            return False
        n += 1
        i += 1
    return True

print(prime_fib(5))  # this will print 89
```