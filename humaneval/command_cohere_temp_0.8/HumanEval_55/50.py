```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
The `fib` function calculates the n-th Fibonacci number iteratively, using a recursive approach. It handles the base cases when `n` is 1 or 0, where it returns `n` directly, and then recursively computes the sum of the (n-1)th and (n-2)th Fibonacci numbers for larger `n`.