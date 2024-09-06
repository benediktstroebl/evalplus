```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
The `fib` function calculates the Fibonacci number for `n` by recursively calling itself with reduced values until it reaches a base case when `n` is 1 or less, at which point it returns `n` itself. This approach is fundamental in building the sequence.