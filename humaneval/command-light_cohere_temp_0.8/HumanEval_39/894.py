```python
import math

def prime_fib(n):
    """
    Returns n-th Fibonacci number and checks if it's prime.
    n = int(math.sqrt(n) + 1)
    if n <= 1:
        return n
    elif n % 2 == 0:
        return prime_fib(n - 2)
    else:
        # Calculate the sqrt of (n+1)
        sqrt_n = int(math.sqrt(n + 1))
        # Check for factors
        factors = [i for i in range(5, sqrt_n, 2)]
        for i in factors:
            if n % i == 0:
                return False
        return n
```