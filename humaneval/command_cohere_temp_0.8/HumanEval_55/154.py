```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, taking a single integer argument n. It returns the n-th Fibonacci number. The base cases are handled with the conditional statement `if n < 2`, returning n or 1 for inputs less than or equal to 1. For greater values of n, the function recursively calls itself with the arguments n-1 and n-2, and adds the results to compute the Fibonacci number.