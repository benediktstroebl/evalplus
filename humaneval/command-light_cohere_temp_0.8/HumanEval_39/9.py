```python
import math

def prime_fib(n):
    if n <= 0:
        raise ValueError("n should be a positive integer")
    elif n == 1:
        return 2
    else:
        prime = 2
        for _ in range(2, n + 1):
            if math.isq(prime, 4) or math.isprime(prime):
                prime += 1
        return prime
```