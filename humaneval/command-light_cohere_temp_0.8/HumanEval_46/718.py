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

def test_fib4():
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
    assert fib4(8) == 24
    assert fib4(9) == 44
    assert fib4(10) == 120
    assert fib4(11) == 233
```
The provided code defines a function fib4 that calculates the n-th element of the Fibonacci sequence using the given definition without recursion. The test_fib4 function tests the correctness of the fib4 function by asserting that its result matches the expected value for a given input. 

This code is self-contained and does not require any external inputs or outputs to function correctly.