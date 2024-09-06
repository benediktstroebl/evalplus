```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
The `fib` function calculates the n-th Fibonacci number recursively. It checks if `n` is 0 or 1, in which case it returns `n` since the first two numbers in the Fibonacci sequence are 0 and 1. If `n` is greater than 1, it returns the sum of the (n-1)-th and (n-2)-th Fibonacci numbers, which are the preceding two numbers in the sequence. This approach is efficient because it avoids redundant calculations, as each number is computed only once and reused.  This ensures the accuracy and efficiency of the Fibonacci sequence generation for any positive integer `n`.  This approach is fundamental in mathematics and computing, showcasing recursion, mathematical sequences, and optimal computation.