```python
def fib4(n: int):
    """The Fibonacci sequence is a series of numbers in which the next number is the sum of the two preceding ones:
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

# Unit tests
def test_fib4():
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0
    assert fib4(4) == 4
    assert fib4(5) == 5
    assert fib4(6) == 8
    assert fib4(7) == 14
    assert fib4(8) == 22

if __name__ == "__main__":
    test_fib4()
```
The code defines a function `fib4` that computes the nth element of the Fibonacci sequence using the given formula. It then provides unit tests to ensure the function's correctness. The `test_fib4` function runs these tests.