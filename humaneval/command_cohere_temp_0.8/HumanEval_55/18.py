```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
The `fib` function uses a recursive approach to calculate the Fibonacci sequence. It bases its action on whether `n` is less than or equal to 1, returning `n` directly in such cases. If `n` is greater than 1, it employs recursive logic, returning the sum of the previous two numbers in the sequence (fib(n-1) + fib(n-2)). This captures the inherent nature of the Fibonacci sequence where each number is the sum of the two preceding ones.