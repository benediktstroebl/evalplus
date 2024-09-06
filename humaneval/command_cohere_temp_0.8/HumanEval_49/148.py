Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function accepts two integers as parameters, namely `n` and `p`, and it returns `2` raised to the power of `n` modulo `p` using the `pow()` function.  Please note that the result will be a modulo value, as described. 

Here's a simple test suite to ensure the function operates as expected:
```python
def test_modp():
    assert modp(0, 101) == 1
    assert modp(3, 5) == 3
    assert modp(1101, 101) == 2
    assert modp(3, 11) == 8
    assert modp(100, 101) == 1

test_modp()
```
This test suite includes several test cases to cover different scenarios of `n` and `p` and expects the output to match the expected result for each test case.  The `modp()` function is then invoked through the call `test_modp()` and the function is expected to pass all test cases, as it's implemented to solve the problem as outlined in the original markdown code block.  This approach ensures the function operates correctly and returns the expected results.  If modifications are made to the function, this test suite will provide feedback on whether the changes introduce any regressions or unexpected behaviour.  This is a recommended approach, rather than manual testing, to ensure full coverage and automation of the testing process.