```python
def fib4(n: int):
    """
    Fibonacci sequence.
    Returns the time on n, using the recurrence relation: fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)
    """
    return 4 * (fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4))
```
Do you have a problem you'd like to solve using Python?