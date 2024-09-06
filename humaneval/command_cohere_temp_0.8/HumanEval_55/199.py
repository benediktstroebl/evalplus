```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
The `fib` function calculates the n-th Fibonacci number recursively. It checks if `n` is less than or equal to 1, returning `n` directly if so. If `n` is greater than 1, it recursively calls itself with `n-1` and `n-2`, adding the results to produce the Fibonacci number for the given input `n`.