```python
import math
def prime_fib(n):
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(n - 2):
        a, b = math.isprime(a + b),b)
    return a
``` 
This function, `prime_fib`, calculates and returns the n-th Fibonacci number that is prime. It utilizes an simple loop to check for primality for each Fibonacci number until the nth.  number is prime, and then returns the nth prime Fibonacci number.