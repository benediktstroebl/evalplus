```python
import math

def prime_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n % 2 == 0:
        return prime_fib(n - 1)
    else:
        return math.isq(2 * prime_fib(n - 2) + 1)
``` 
This function calculates the n-th Fibonacci number that is also prime, using a simple recursive approach. 
Let me know if there is anything else I can help you with!