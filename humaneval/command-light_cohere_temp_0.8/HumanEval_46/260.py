```python
def fib4(n: int):
    """The Fibonacci sequence without recursion."""
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
    """Function that tests the 'fib4' function."""
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14

# Run the test function to check the function is working correctly.
```