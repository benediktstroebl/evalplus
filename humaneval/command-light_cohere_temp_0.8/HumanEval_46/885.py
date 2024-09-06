```python
def fib4(n: int):
    """The Fibonacci sequence 4 number sequence is defined as follows:
    Returns the n-th element of the Fibonacci sequence 4."""
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    elif n == 4:
        return 2
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fib4():
    """Test the fib4 function"""
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14

if __name__ == "__main__":
    test_fib4()
```
The code defines a function called `fib4()` that computes the nth element of the Fibonacci sequence 4. It adheres to the pattern of the sequence where each number is the sum of the preceding three numbers. The test function `test_fib4()` is used to verify the correctness of the `fib4()` function by passing various test cases.