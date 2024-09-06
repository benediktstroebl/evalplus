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
    """Test the fib4 function."""
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14

    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0
    assert fib4(4) == 4
    assert fib4(5) == 5
    assert fib4(6) == 6
    assert fib4(7) == 7

    assert_equal(fib4(8), 8)
    assert_equal(fib4(9), 37)

if __name__ == "__main__":
    test_fib4()
```
The code defines a Fibonacci sequence generator using a loop. The fib4 function takes an parameter n, representing the position in the sequence, and returns the corresponding Fibonacci number. The test_fib4 function tests the fib4 function by passing different values to it and asserting that the returned values are correct. 

The output of this code is the result of running the test_fib4 function, which will print the output of the fib4 function for different input values.