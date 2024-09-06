```python
def fib4(n: int):
    """The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones.
    if n < 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fib4():
    """Test the fib4 function."""
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0
    assert fib4(4) == 4
    assert fib4(5) == 5
    assert fib4(6) == 8
    assert fib4(7) == 14
    assert fib4(8) == 28
    assert fib4(9) == 56

if __name__ == "__main__":
    test_fib4()
```
The Python script defines a function called fib4 which computes the n-th element of the Fibonacci sequence using a loop. The function also implements a test suite that verifies the correctness of the function. 

We can call the `test_fib4()` function to run all the tests.