```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, taking a single argument n, which returns the nth Fibonacci number. The base case checks if n is less than or equal to 1, in which case it returns n, as the first two Fibonacci numbers are 0 and 1. Otherwise, it recursively calls itself with arguments n-1 and n-2, adding the results to compute the subsequent Fibonacci number and returns it.