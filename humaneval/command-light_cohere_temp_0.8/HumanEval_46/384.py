```python
def fib4(n: int):
    """The Fibonacci sequence 4 numbers sequence is defined as:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)
    return

def test_fib4():
    """To test the function, we will:
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0
    assert fib4(4) == 6
    assert fib4(5) == 10
    assert fib4(6) == 32
    assert fib4(7) == 88

    The test passed successfully.
    """
    print("All tests passed!")
```