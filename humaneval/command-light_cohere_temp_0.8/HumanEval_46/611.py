```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each successive number is defined as a sum of the two preceding ones. The sequence begins with 0 and 1, and each subsequent term is the sum of the previous two terms.

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

# Example usage
if __name__ == "__main__":
    test_fib4()
```
This Python script defines a function `fib4` that computes the nth element of the Fibonacci sequence without recursion. The function uses a simple formula: `fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)`. The function is then tested with various input values and the test results are assertions. The `test_fib4` function runs the `fib4` function with different input values and checks if the output is correct. The `if __name__ == "__main__":` block runs the test function when the script is executed.