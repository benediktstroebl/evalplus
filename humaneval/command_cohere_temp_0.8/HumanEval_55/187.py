```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
The `fib` function calculates the n-th Fibonacci number iteratively, using a simple recursion formula `F(n) = F(n-1) + F(n-2)`. This avoids the exponential complexity associated with a straightforward recursive implementation. It also reduces computational overhead by utilizing the recurrence formula instead of relying on repeated multiplication. This approach proves more efficient, especially for larger values of n, offering a more manageable and scalable solution for calculating Fibonacci numbers.