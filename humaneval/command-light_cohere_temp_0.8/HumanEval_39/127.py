```python
import math
def prime_fib(n):
    """
    Return the n-th Fibonacci number that is prime.
    return the prime_fib(1): 2
    """
    if n == 1:
        return 2
    else:
        # Check if n is a perfect square
        sqrt_n = math.sqrt(n)
        if sqrt_n*sqrt_n == n:
            return 2
        else:
            # Fibonacci number and not prime, return n
            return n
```