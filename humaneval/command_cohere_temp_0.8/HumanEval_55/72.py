```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
The `fib` function calculates the n-th Fibonacci number iteratively, using a recursive approach. It checks if `n` is 0 or 1, in which case it returns `n` since the first two numbers in the Fibonacci sequence are 0 and 1. If `n` is greater than 1, it recursively calls itself with `n-1` and `n-2`, adding the results to produce the next Fibonacci number.