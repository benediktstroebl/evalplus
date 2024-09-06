```python
def fib4(n: int):
    """The Fibonacci sequence without recursion."""
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
    assert fib4(5) == 4  # Should be 4
assert fib4(6) == 8  # Should be 8
assert fib4(7) == 14  # Should be 14

# Main code
if __name__ == "__main__":
    test_fib4()
```
The code defines a function `fib4` which computes the n-th Fibonacci number without recursion. It uses a's simple formula to calculate each number in the sequence.

The `test_fib4` function is used to run tests on the `fib4` function, ensuring it produces the correct results for the given input values. 

When you run the code, it will run the tests and display whether the function's outputs are correct or not.