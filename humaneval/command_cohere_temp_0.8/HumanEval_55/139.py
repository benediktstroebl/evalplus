```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
The code defines a recursive function `fib` that calculates the n-th Fibonacci number by recursively calling itself with values `n-1` and `n-2` and returning their sum, or returning `n` if `n` is less than or equal to 1.