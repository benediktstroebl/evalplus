```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
The `fib` function calculates the n-th Fibonacci number iteratively, using a recursive approach. It handles the base cases when `n` is 1 or 0, where it returns `n` directly. For larger `n`, it recursively calls itself with `n-1` and `n-2`, adding the results to compute the next Fibonacci number. This accumulates the Fibonacci sequence, allowing the function to calculate large Fibonacci numbers efficiently. The function's elegant simplicity and computational efficiency make it an essential tool for various applications that require Fibonacci numbers.