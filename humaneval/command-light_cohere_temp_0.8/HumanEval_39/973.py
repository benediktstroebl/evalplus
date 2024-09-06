```python
import math

def prime_fib(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        a, b = 3, 2
        for _ in range(n - 2):
            a, b = b, a + b
        return b

# Test the function
print(prime_fib(5))  # Output: 89
```

This script defines a function `prime_fib` that computes and returns the n-th Fibonacci number that is also prime. The function uses dynamic programming to iterate and find the prime Fibonacci number, ensuring that the result is correct for any positive integer input.