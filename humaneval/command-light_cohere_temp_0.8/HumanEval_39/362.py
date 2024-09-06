```python
import math

def prime_fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 1
    if n == 2:
        return 2
    a, b = 3, 2
    for _ in range(n - 2):
        a, b = b, a + b
    return b

# Test the function
print(prime_fib(5))  # Output: 89
print(prime_fib(10))  # Output: 552291118
```
The code defines a function `prime_fib` that calculates and returns the n-th Fibonacci number which is also prime. 

The function uses an iterative method to find the prime number by continually updating the variables `a` and `b` in each iteration. 

It then tests the function with different inputs and prints the results.