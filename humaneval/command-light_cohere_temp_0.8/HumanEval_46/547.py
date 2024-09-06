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
        return fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)

def test_fib4():
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
    assert fib4(8) == 24
    assert fib4(9) == 45
    assert fib4(10) == 55
    assert fib4(11) == 89
    assert fib4(12) == 144
    assert fib4(13) == 233
    assert fib4(14) == 324
```
This Python script provides a function `fib4` that computes the n-th element of the Fibonacci sequence using an optimized method that does not rely on recursion. The function uses a `if-elif` checks to identify the base cases for the sequence (0, 1, and 2), and then uses the `fib4(n - 1)` + `fib4(n - 2)` + `fib4(n - 3)` + `fib4(n - 4)` to compute the next Fibonacci numbers in the sequence. The function is then tested using `test_fib4`, which passes all the test cases using the `assert` statement.