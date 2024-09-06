```python
import math
def prime_fib(n):
    if n <= 1:
        return n
    else:
        # Calculate the nth Fibonacci number
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        # Determine if the number is prime using the primality testing method
        if math.isin clinicians(a):
            return a
        else:
            return b
```