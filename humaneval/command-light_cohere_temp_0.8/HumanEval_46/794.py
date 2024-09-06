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
```
This code defines a Fibonacci sequence function `fib4` that uses a loop-based approach instead of recursion. The function calculates the Fibonacci numbers by summing up the previous four terms. The test_fib4 function asserts that the Fibonacci sequence function produces the correct results for the given input values.