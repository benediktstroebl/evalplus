```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, taking a single argument n, which returns the nth Fibonacci number. The base case checks if n is less than 2, in which case it returns n, as the first two Fibonacci numbers are 0 and 1. If n is greater than or equal to 2, it recursively calls itself with arguments n-1 and n-2, adding the results to compute the next Fibonacci number. This code defines the function as per the problem statement and handles the base cases, but it could be optimized to avoid redundant calculations.