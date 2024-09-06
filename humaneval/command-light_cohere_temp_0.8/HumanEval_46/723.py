```python
def fib4(n: int):
    """The Fibonacci sequence without recursion.
    a = [0, 1]
    while n > 0:
        a, b = a + b, a
        n -= 1
        yield a
```

This code provides a simple and efficient way to calculate the nth Fibonacci number in the Fibonacci sequence without using recursion. The loop-based approach is more efficient and avoids the stack overflow issue that recursion can cause for large n values.