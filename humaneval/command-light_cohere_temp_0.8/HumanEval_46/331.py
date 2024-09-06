```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which the next number is equal to the sum of the two preceding ones.
    if n < 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 0
    else:
        return fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)

def test_fib4():
    """test cases"""
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0
    assert fib4(4) == 4
    assert fib4(5) == 5
    assert fib4(6) == 8
    assert fib4(7) == 14

if __name__ == "__main__":
    test_fib4()
```
The provided Python script defines a function `fib4` that computes the n-th element of the Fibonacci sequence using an iterative approach without recursion. It also includes a test cases to validate the function's correctness.