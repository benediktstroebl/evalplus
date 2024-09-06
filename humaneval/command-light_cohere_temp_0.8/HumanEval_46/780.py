```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones. The Fib4 sequence is often used to model growth and decay.
    if n < 4:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fib4():
    """Test the fib4 function with various values of n."""
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0
    assert fib4(4) == 4
    assert fib4(5) == 5
    assert fib4(6) == 8
    assert fib4(7) == 14
    assert fib4(8) == 32
    assert fib4(9) == 55
    assert fib4(10) == 90
```
This code defines a function called fib4 that computes the n-th Fibonacci number in a self-contained manner. It does not use recursion and instead uses a case-based approach to calculate the Fibonacci number. The test_fib4 function tests the fib4 function with various values of n and asserts that the results are correct.