```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test cases
test_max_element = [
    ( [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], max_element),
    ( [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], None),
    ( [1, 2, 3, 4, 5, 6, 7, 8, 9], float('inf')),
    # Complex case with negative and zero
    ([-5, 0, -10], max_element),
    # empty list
    ([], max_element),
    # Complex list with negative numbers
    [1, 2, 3, -4, 5], float('inf')),
]

# Main function to run the tests
def test_function():
    """Execute all test cases"""
    for (test_data, expected_result) in test_max_element:
        result = max_element(test_data)
        assert result == expected_result, f"Test {test_data} failed"

# Run the tests
test_function()
 ```
This script defines a max_element function, which finds the maximum element in a given list. The test_max_element list contains a set of test cases, each consisting of a list of data and the corresponding function call with that data. The test_function function iterates through each test case and checks if the result from max_element matches the expected result using the assert statement.