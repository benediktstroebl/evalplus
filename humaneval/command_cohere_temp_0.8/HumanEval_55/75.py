```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
The code defines a recursive function `fib` that calculates the n-th Fibonacci number by invoking itself recursively on `n-1` and `n-2`, then adding the results. This mimics the classic definition of Fibonacci numbers: Fib(n) = Fib(n-1) + Fib(n-2). It accounts for the base cases of `n` equal to 1 or less than 1, where it directly returns `n` or `n-1`, respectively.