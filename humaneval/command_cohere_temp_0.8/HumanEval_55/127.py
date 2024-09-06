```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
The code defines a recursive function fib that takes an integer n as input and returns the n-th Fibonacci number. The base cases are handled with the condition `if n < 2`, returning n or 2 for n=1 or n=2 respectively. For larger values of n, the function recursively calls itself with the arguments (n-1) and (n-2), representing the Fibonacci sequence backward, and adds the results to compute the Fibonacci number.