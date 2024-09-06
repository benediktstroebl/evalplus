```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
The `fib` function implements the recurrence relation of the Fibonacci sequence: `F(n) = F(n-1) + F(n-2)`. This relation holds for the Fibonacci sequence, where the `n`-th term is the sum of the two preceding terms. It defaults to returning the value for `n` <= 1, which are the base cases for the recursion.