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
    n = 5
    assert fib4(n) == 4
    n = 6
    assert fib4(n) == 8
    n = 7
    assert fib4(n) == 14
```

This script defines a function `fib4` that computes the nth element of the Fibonacci sequence using a loop-free approach. The `test_fib4` function tests the `fib4` function with various input values and asserts that the results are correct. 

Then, the Fibonacci sequence is calculated using the `fib4` function, and the results are compared against the expected values.