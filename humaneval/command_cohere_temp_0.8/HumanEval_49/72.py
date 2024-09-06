```python
def modp(n, p):
    return pow(2, n, p)
```

This Python expression employs the built-in `pow` function to calculate `2` raised to the power of `n` modulo `p`. This function inherently handles the modulo arithmetic, making it a concise and efficient solution.

Here is a test script that can be used to verify the correctness of the solution:
```python
def test_modp():
    assert modp(0, 101) == 1
    assert modp(3, 5) == 3
    assert modp(1101, 101) == 2
    assert modp(3, 11) == 8
    assert modp(100, 101) == 1

test_modp()
```

This test script contains several test cases that cover different scenarios and edge cases. Each test case asserts that the output of the `modp` function is as expected.

When the `modp` function is called with different input values, the test suite will automatically verify that the output matches the expected output. If all the tests pass, it indicates that the `modp` function is correctly implemented and complies with the problem statement.

To execute the test suite, save the Python script in a directory or module and initiate it using the Python interpreter:
```bash
python test_modp.py
```

The test suite will execute concurrently against the `modp` function. If all tests succeed, you will observe the "OK" indication, confirming that the function resolves the problem accurately.

This comprehensive test suite ensures the `modp` function's correctness against diverse scenarios and maintains the code's adherence to the problem statement.