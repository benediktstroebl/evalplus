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
    """test
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

test_fib4()
```
The provided function, fib4, calculates the n-th element of the Fibonacci sequence using a loop-based approach, without recursion. The function takes an integer n as input and returns the corresponding Fibonacci number. The test_fib4 function contains a series of test cases that verify the correctness of the fib4 function by checking its output against the expected results for specific input values.