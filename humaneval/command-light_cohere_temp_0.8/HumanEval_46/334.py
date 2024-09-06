```python
def fib4(n: int):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

# Unit tests
import pytest

def test_fib4():
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
```
The function `fib4` takes an integer `n` as an argument and returns the 4th element of the Fibonacci sequence using the provided formula. The function also has a series of tests that cover different input values. The tests pass successfully, confirming the correctness of the function.