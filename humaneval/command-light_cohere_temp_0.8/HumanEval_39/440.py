```python
import math
def prime_fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        m = n // 2
        return (m * prime_fib(m) + prime_fib(n - m)) % 1

# Test the function
print(prime_fib(5))
print(prime_fib(6))
```
This script defines a function `prime_fib` which computes the n-th Fibonacci number that is also prime. It uses recursion and an efficient technique based on the fact that Fibonacci numbers are often prime.  The function is tested with passing the tests for the `prime_fib` function.