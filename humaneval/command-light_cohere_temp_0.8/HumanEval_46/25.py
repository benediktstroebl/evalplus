```python
def fib4(n: int):
    """The Fibonacci sequence without recursion.
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fib4():
    """Test the fib4 function"""
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0
    assert fib4(4) == 4
    assert fib4(5) == 5
    assert fib4(6) == 8
    assert fib4(7) == 14
    assert fib4(8) == 28
    assert fib4(9) == 44
    assert fib4(10) == 120
```

This code defines a function `fib4` that computes the n-th Fibonacci number in the sequence without recursion. The `test_fib4` function is used to test the correctness of the `fib4` function with various input values.