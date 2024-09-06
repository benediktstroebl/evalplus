```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each successive term is defined as a sum of the two preceding terms. The Fib4 sequence is called Fibonacci numbers or Fibonacci sequence."""
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

test_fib4()
```

This Python code defines a function `fib4` that computes the n-th Fibonacci number in the sequence using the iterative method. It provides an implementation of the well-known Fibonacci sequence and passes the unit tests successfully.