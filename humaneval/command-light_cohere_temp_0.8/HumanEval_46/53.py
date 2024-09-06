```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones.
    if n < 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b

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
```

This code defines a function `fib4` that computes the n-th element of the Fibonacci sequence using an iterative approach. The function uses a simple loop to calculate each number in the sequence by summing the two preceding numbers. 

The `test_fib4` function contains a set of assertions that validate the function's correctness for various input values.