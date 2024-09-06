```python
def fib4(n: int):
    """The Fibonacci sequence without recursion.
    a = [0, 1]
    while n > 0:
        a, b = a + b, a
        n -= 1
        yield a  # Return the value at each step

def test_fib4():
    n = 7
    assert fib4(n) == 14
```