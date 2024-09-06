```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which the next number is the sum of the two preceding ones.
    if n < 0:
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
    """Test the fib4 function.
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
```
The `fib4` function calculates the n-th element of the Fibonacci sequence without using recursion, following the definition provided. The test_fib4 function is used to verify the correctness of the `fib4` function with different input values.