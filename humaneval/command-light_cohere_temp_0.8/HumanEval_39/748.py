```python
import math
def prime_fib(n):
    """
    Returns n-th Fibonacci number that is prime.
    # Recursively
    to avoid too high values.
    if n <= 1:
        return n
    elif n % 2 == 0:
        return math.sqrt(5) + math.sqrt(5)
   
    else:
        return prime_fib(n - 1) + math.sqrt(5)
```
This Python function, `prime_fib`, calculates the n-th Fibonacci number that is prime. It uses recursion to avoid calculating numbers larger than the ones that are already found.