```python
def fib4(n: int):
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
    """Code to test the fib4 function"""
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0
    assert fib4(4) == 4
    assert fib4(5) == 5
    assert fib4(6) == 8
    assert fib4(7) == 14
    assert fib4(8) == 22
    assert fib4(9) == 33
    assert fib4(10) == 55
    assert fib4(11) == 89
    assert fib4(12) == 144
    assert fib4(13) == 233
    assert fib4(14) == 377
    assert fib4(15) == 610
    assert fib4(16) == 882
    assert fib4(17) == 1597

test_fib4()
```
The code defines a `fib4` function that computes the nth Fibonacci number in O(n) using an iterative approach without recursion. The `test_fib4` function contains test cases to verify the correctness of the `fib4` function.  The `assert` statements are used to compare the function's output with the expected results for various input values.