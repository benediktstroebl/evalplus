```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
The `fib` function uses a recursive approach to calculate the Fibonacci sequence. It bases its solution on two main cases:
1. If `n` is less than or equal to 1, it returns `n` directly as the base case of the Fibonacci sequence (0 and 1 are the first two numbers in the sequence).
2. If `n` is greater than 1, it returns the sum of the two previous Fibonacci numbers (obtained by recursively calling the function with `n-1` and `n-2`).

This approach allows the function to calculate the nth Fibonacci number without the need for explicit intermediate storage.