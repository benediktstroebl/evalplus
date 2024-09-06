```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, taking a single integer n as input. It returns the n-th Fibonacci number. The base cases are handled with the simple condition n < 2, where it returns n directly if n is 1 or 0. If n is greater than or equal to 2, the function recursively calls itself with the arguments n-1 and n-2, adding the results to compute the Fibonacci number for the given input.