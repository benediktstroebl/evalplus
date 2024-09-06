```python
import math
def prime_fib(n):
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(2, n + 1):
        a, b = math.isprime(b),isprime(a)
        if a == b:
            continue
        else:
            yield a
            yield b
``` 
The function `prime_fib` generates and returns the n-th Fibonacci number that is prime, or returns n itself if it's not a prime.