```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones:
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fib4():
    """Test function for fib4.
    n = 5
    assert fib4(n) == 4
    n = 6
    assert fib4(n) == 8
    n = 7
    assert fib4(n) == 14

test_fib4()
```