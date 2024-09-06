```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, taking a single integer n as input. It returns the n-th Fibonacci number. The base cases are handled with the conditional statement `if n < 2`, returning n or 1 for the first two indices. For larger values of n, the function recursively calls itself with the arguments (n-1) and (n-2), representing the recursive nature of the Fibonacci sequence where each number is the sum of the two preceding ones.