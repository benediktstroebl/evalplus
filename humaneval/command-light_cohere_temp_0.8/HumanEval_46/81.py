```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones.
    if n < 2:
        return 2
    elif n == 3:
        return 0
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fibonacci4(n: int):
    """Test the fib4 function with different input values."""
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0
    assert fib4(4) == 4
    assert fib4(5) == 5
    assert fib4(6) == 8
    assert fib4(7) == 14
    assert fib4(8) == 28
    assert fib4(9) == 34

if __name__ == "__main__":
    test_fibonacci4(10)
```
This script defines a function `fib4` that computes the nth element of the Fibonacci sequence using a simple summation-based approach. The `test_fibonacci4` function is used to run tests on the `fib4` function with different input values. 
When you run the script, it will execute the test suite and provide feedback on whether the function's output matches the expected results for various input values. 
This approach is self-contained, meaning it doesn't rely on any external libraries or functions and can be fully contained within the script.