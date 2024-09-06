```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, which takes an integer n as input. It returns the nth Fibonacci number. The base cases are handled with the condition `if n <= 1:`, where it returns n if n is either 1 or 0, assuming the first two Fibonacci numbers are 0 and 1. If n is greater than 1, it recursively calls itself with the arguments n-1 and n-2, and adds the results to compute the Fibonacci number for n.