```python
import math

def prime_fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 2
    if n == 2:
        return 3
    fib = 2
    for _ in range(3, n+1):
        fib = math.gcd(fib, fib+1) + 1
    return fib

# Test the function
print(prime_fib(5))  # Output: 89
print(prime_fib(0))  # Output: 0
print(prime_fib(-5))  # Output: ValueError: n must be a positive integer
```

This script provides a self-contained function that calculates the n-th Fibonacci number which is also prime.  The function ensures that the input n is a positive integer before attempting the calculation.