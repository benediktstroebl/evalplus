```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, taking a single argument n, which returns the nth Fibonacci number. The base case checks if n is less than or equal to 1, in which case it returns n as the first two numbers in the Fibonacci sequence are 0 and 1. If n is greater than 1, the function recursively calls itself, with arguments n-1 and n-2, and adds the results to produce the next Fibonacci number. This recursion continues until n is <= 1, at which point the base case takes over and returns the final result.