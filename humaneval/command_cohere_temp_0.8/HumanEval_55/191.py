```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
The `fib` function calculates the n-th Fibonacci number iteratively, using a simple recurrence relationship. It handles the base cases when `n` is 1 or 0, returning `n` directly, and otherwise, it recursively calls itself with `n-1` and `n-2` to calculate the Fibonacci number for any other value of `n`.  This approach is efficient because each number is computed only once and reused throughout the calculation.