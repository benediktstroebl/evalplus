```python
import math
def prime_fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # Using the goldberg - murphy primality sequence
        a, b = 3, 2
        for _ in range(n - 2):
            a, b = b, a + b
        return b
```