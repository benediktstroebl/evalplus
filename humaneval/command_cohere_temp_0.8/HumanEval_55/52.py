```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
The code defines a recursive function `fib` that calculates the n-th Fibonacci number. It checks if `n` is 0 or 1, in which case it returns `n` since the first two numbers in the Fibonacci sequence are 0 and 1. For `n` greater than 1, it recursively calls itself with `n-1` and `n-2`, adding the results to compute the next Fibonacci number.