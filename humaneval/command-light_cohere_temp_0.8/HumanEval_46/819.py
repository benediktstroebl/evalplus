```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones. The sequence starts with 0 and 1 and grows exponentially.
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
    """Test the fib4 function."""
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
```
This script defines a function `fib4` that computes the n-th element of the Fibonacci sequence using the formula `fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)`. The `test_fib4` function tests the `fib4` function by asserting that its result is correct for a given input `n`.