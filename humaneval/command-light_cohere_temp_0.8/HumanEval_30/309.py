```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test the function with a list of values and expected output
def test_get_positive():
    inputs = [
        [-1, 2, -4, 5, 6],
        [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
    ]

    expected = [
        [2, 5, 6],
        [5, 3, 2, 3, 9, 123],
        []
    ]

    for test in inputs:
        actual = get_positive(test)
        assert actual == expected, "Actual: " + str(actual) + ", Expected: " " + str(expected) + "\n"

# Test the function with a tuple of input and expected output
def test_tuple_get_positive():
    inputs = (
        [-1, 2, -4, 5, 6],
        [2, 5, 6],
        [-5, 3, -3, 9]
    )

    expected = (
        [2, 5, 6],
        [5, 3, 2, 3, 9],
        []
    )

    for test, expected_output in zip(inputs, expected):
        actual_output = get_positive(test)
        assert actual_output == expected_output, "Test: " + str(test) + ", Expected: " + str(expected_output) + "\n"

# Run the function and print the output
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])))
```
This script defines a function `get_positive` that filters out negative numbers from an input list. The `test_get_positive` function contains various test cases for the `get_positive` function: Finally, the script calls the `get_positive` function with a list of values and prints the output, which should match the expected output based on the test cases.