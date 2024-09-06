```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
The code defines a Python function called `fib` that calculates the n-th Fibonacci number. The base case checks if `n` is less than or equal to 1, in which case it returns `n` since the first two Fibonacci numbers are 0 and 1. Otherwise, the function recursively calls itself to calculate the Fibonacci numbers for `n-1` and `n-2` and adds them together to provide the Fibonacci number for the given input `n`.