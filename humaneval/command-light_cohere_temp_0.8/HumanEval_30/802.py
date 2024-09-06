```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test cases
tests = [
    [
        {
            "input_data": [-1, 2, -4, 5, 6],
            "expected_output": [2, 5, 6]
        },
        {
            "input_data": [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
            "expected_output": [5, 3, 2, 3, 9, 123, 1]
        },
        # Add more test cases as needed
    ]

# Run the function and verify the tests
for test in tests:
    actual_output = get_positive(test["input_data"])
    assert actual_output == test["expected_output"]
 ``` 
This code defines a function `get_positive` that takes a list as input and returns a new list with only the positive numbers from the original list. The function uses list comprehension to filter out the positive numbers. The script also includes a list of test cases, each containing input data and an expected output. The test cases are verified by running the `get_positive` function with the input data and comparing the actual output to the expected output.