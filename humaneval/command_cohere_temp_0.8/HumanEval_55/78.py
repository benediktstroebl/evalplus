```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python function uses a recursive approach to calculate the Fibonacci sequence. It bases its action on two key cases:
1. If `n` is less than 2 (which means it's computing a number before the sequence starts), it returns `n` as the answer (since the first two Fibonacci numbers are 0 and 1).
2. If `n` is greater than or equal to 2, it recursively calls itself with the arguments `n-1` and `n-2`, and adds the results together. This is the core Fibonacci calculation, where each number is the sum of the two preceding ones.