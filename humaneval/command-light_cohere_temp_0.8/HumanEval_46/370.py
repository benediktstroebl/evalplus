```python
def fib4(n: int):
    """The Fibonacci sequence without recursion.
    a = [0, 1]
    while n > 0:
        a, b = a+b, a
        n -= 1
        yield a  # Return the value of the next Fibonacci number and yield a statement to be executed next
```