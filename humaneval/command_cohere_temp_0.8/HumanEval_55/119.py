```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
The `fib` function uses recursion to compute the `n-th` Fibonacci number. This is verified and confirmed by the unit tests available in the original problem statement.