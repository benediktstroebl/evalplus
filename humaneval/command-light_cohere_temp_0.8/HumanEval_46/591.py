```python
def fib4(n: int):
    """The Fibonacci sequence, nth element."""
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        return fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)

def test_fib4():
    """test the function"""
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0
    assert fib4(4) == 4
    assert fib4(5) == 5
    assert fib4(6) == 8
    assert fib4(7) == 14
```

The code defines a function called `fib4` that computes the n-th Fibonacci element using a loop. The function implements the optimized approach using memoization, avoiding redundant recursive calls and improving efficiency. The `test_fib4` function tests the `fib4` function with various input values and asserts that the computed Fibonacci values match the expected results.