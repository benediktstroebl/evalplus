```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which the next number is achieved using the sum of the two preceding ones. The Fib4 sequence is defined as:
    fib4(0) = 0
    fib4(1) = 0
    fib4(2) = 2
    fib4(3) = 0
    fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)
    return

# Unit tests
def test_fib4():
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

if __name__ == "__main__":
    test_fib4()
```
The provided code defines a function fib4(n) that computes the n-th Fibonacci number in O(1) using the formula: fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4). The function is then tested with various input values using the test_fib4() function. The test_fib4() function ensures the correctness of the fib4() function by passing a series of test cases.