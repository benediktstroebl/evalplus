```python
import math
def prime_fib(n):
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(n - 2):
        a, b = math.next_prime(b),
    c = a + b
    return c
``` 
This function calculates and returns the n-th Fibonacci number that is prime.