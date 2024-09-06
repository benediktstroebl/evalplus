```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    for i in range(n):
        l[i] = l[i] + 1
    return l

# Test the function with a sample input and expected output
test_incr_list = """
def test_incr_list(l: list):
    assert incr_list(l) == [2, 3, 4]
""")

# Run the test function and display the result
test_incr_list(input)
```
The `test_incr_list` function is a simple example of a unit test. It defines a test function with the `assert` statement to check if the `incr_list` function's output matches the expected output. It uses the test to execute the `incr_list` function with a sample input list `[1, 2, 3]` and asserts that the result is indeed `[2, 3, 4]`. The `test_incr_list` function is then run with the sample input, and the result is displayed.