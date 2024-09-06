```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones.
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

def test_fib4():
    """Test the fib4 function. Test it with different values of n, where n is a positive integer."""

    # Test with different values of n
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14

    # Test with invalid input (n < 0)
    with pytest.raises("n must be a >= 0"):
        assert not fib4(-1)

    # Test with invalid input (n > 7)
    with pytest.raises("n must be less than 7"):
        assert not fib4(8)

# Run the tests
if __name__ == "__main__":
    test_fib4()
```

This Python script defines the `fib4` function, which computes the n-th element of the Fibonacci sequence without recursion. The `test_fib4` function contains tests that verify the correctness of the `fib4` function with various input values. The script uses the `pytest.assert` for creating tests tests, which are executed automatically when the script is run. The final line `if __name__ == "__main__":` ensures that the tests are executed only when the script is run directly, not when it's imported as a module.