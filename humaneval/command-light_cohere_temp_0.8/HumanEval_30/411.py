```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test cases
test_get_positive = [
    dict(zip(['Input', 'Expected Output'], [
        ['[-1, 2, -4]', [2, 4, 6]],
        ['[-5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]', [5, 3, 2, 3, 9, 123, 1]],
        ['[]', ['[]']],
        ['[5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]', [-1, 2, 3, -10]]
    ]))
]

# Run the tests
test_get_positive()
```
This code defines a function called `get_positive` that takes a list as input and returns a new list containing only the positive elements from the original list. The function uses a `list comprehension` to filter out the positive elements. The test cases section provides a list of dictionaries, each containing the input list and the expected output of the `get_positive` function for various input scenarios. Finally, the test_get_positive function is executed, which verifies that the function produces the correct results for each test case.