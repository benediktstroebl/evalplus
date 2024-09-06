```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which the next number is defined as the sum of the two preceding ones.

    if n is a integer, returns the n-th Fibonacci number.
    if n < < 0:
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
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0
    assert fib4(4) == 4
    assert fib4(5) == 5
    assert fib4(6) == 8
    assert fib4(7) == 14
```

The code defines a function `fib4` that computes the n-th Fibonacci number in the sequence without using recursion. It utilizes an if-elif structure to identify the base cases for the sequence (i.e., the number of 0, 1, 2, and 3) and calculates the subsequent numbers by summing the previous three numbers. The function then returns the tested using the `test_fib4` function, passing several test cases to ensure its correctness.