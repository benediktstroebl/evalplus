```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, which takes an integer n as input. It returns the nth Fibonacci number. The base cases are handled with the simple condition n <= 1, where it returns n if n is either 1 or 0, since the first two numbers in the Fibonacci sequence are 0 and 1. If n is greater than 1, the function recursively calls itself with the arguments n-1 and n-2, and adds the results to produce the nth Fibonacci number. This script provides a straightforward implementation of the Fibonacci sequence as requested.