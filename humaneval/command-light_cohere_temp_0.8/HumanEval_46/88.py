```python
def fib4(n: int):
    """The Fibonacci sequence, except without recursion.
    a = 0
    b = 1
    while n > 0:
        c = a + b
        a, b = b, c
        n -= 1
    return c
```