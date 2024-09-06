```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which the next number is the sum of the two preceding ones.
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fib4():
    """Test the fib4 function.
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
```

This code defines a function `fib4` that computes the nth element of the Fibonacci sequence using a loop-free approach. The function takes an integer n as input and returns the corresponding Fibonacci number. The test function `test_fib4` verifies that the `fib4` function produces the correct results for the given inputs.