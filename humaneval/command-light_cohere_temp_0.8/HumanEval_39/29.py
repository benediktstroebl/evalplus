```python
import math
def prime_fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        m = n**(0.5)
        if math.isQ(m, 0. I == n):
        else:
            a, b = prime_fib(int(m/2)) , prime_fib(int(m%2))
            c = a + b
            return c
```