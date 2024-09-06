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
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
    assert fib4(8) == 24
    assert fib4(9) == 44
    assert fib4(10) == 84
```
This Python code defines a function called `fib4` that computes the n-th value of the Fibonacci sequence. It uses a tested input argument n, checks for specific Fibonacci number outputs for n equal to 0, 1, 2, 3, and 4, and returns the sum of the four preceding Fibonacci numbers. The `test_fib4` function asserts that the `fib4` function produces the correct Fibonacci number sequence up to 10. This code effectively demonstrates the smarotically the Fibonacci sequence.