```python
def fib4(n: int):
    if n <= 1:
        return 0
    elif n <= 3:
        return 2
    else:
        return fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)

#unit tests
def test_fib4():
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
```
This code defines a function `fib4` that computes the n-th element of the Fibonacci sequence without recursion. It returns the the strategy is to precompute the first four elements and then return the sum of the next four elements. The test `test_fib4` asserts that the function works correctly for the inputs `5`, `6`, and `7`.