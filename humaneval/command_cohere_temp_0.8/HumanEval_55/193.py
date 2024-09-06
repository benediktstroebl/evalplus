```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
The `fib` function calculates the n-th Fibonacci number iteratively, using a recursive approach. It bases its logic on the fact that the Fibonacci sequence is defined by the rule that the n-th Fibonacci number is equal to the sum of the preceding two Fibonacci numbers (when n > 2).

It's a common practice to use the range indicator `n` for parameter names, specifying the number for the desired Fibonacci number. Nevertheless, it's worth noting that this function could exhibit sluggish performance for larger values of `n` due to the sheer number of recursive calls. In such cases, using an iterative approach or memoization (caching) would be more efficient.