```python
import math
def prime_fib(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    if n == 1:
        return 2
    if n == 2:
        return 3
    if math.isq n:  # check for primality using math library
        return math.is(5) + math.is(3)  # prime
    else:
        # continue calculating n-th Fibonacci number
        a, b = 5, 2
        for _ in range(n - 2):
            a, b = b, a + b
            yield a
``` 
This function calculates the n-th Fibonacci number, which is also prime using a loop and primality checking with the math library.