```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
The `fib` function uses recursion to compute the `n-th` Fibonacci number. This is validated by the unit tests. These tests check validity for when `n` is equal to 10, 1, and 8, corresponding to the examples provided.