```python
def fib4(n: int):
    """The Fibonacci sequence without recursion.

    a = 0
    b = 1
    for _ in range(n):
        a, b = a + b, a
        yield a 

def test_fib4():
    """Test the function for different values of n."""
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0
    assert fib4(4) == 4
    assert fib4(5) == 5
    assert fib4(6) == 8
    assert fib4(7) == 14
    assert fib4(8) == 32
    assert fib4(9) == 55
    assert fib4(10) == 130
```

The provided code defines a Python function called fib4, which computes the Fibonacci sequence up to the nth element without using recursion. It does this by initializing two variables a and b with the first two Fibonacci numbers, and then iteratively calculating the next Fibonacci numbers by adding the current values of a and b and storing the result in a. exposed then yields the value of a, which is the nth Fibonacci number in the sequence.