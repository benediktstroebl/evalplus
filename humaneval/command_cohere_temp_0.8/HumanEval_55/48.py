```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
The `fib` function implements the recursive formula for Fibonacci numbers. It returns the `n`-th Fibonacci number by recursively calling itself to calculate the two preceding Fibonacci numbers and adding them together. It handles the base cases when `n` is 1 or less than 1, directly returning `n` or `1` respectively.  This approach leads to a linear time complexity of `O(n)` as the number of recursive calls decreases over time, mitigating the potential exponential complexity stemming from an improper implementation.