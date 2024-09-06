```python
def get_positive(l: list):
    return [x for x in l if x >= 0]

# Test the function with different inputs
test_get_positive_inputs = [
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
    [-1, 2, 4, 5, 6],
    [123, -123]
]

# Call the function and compare the results with the test inputs
for test_input, expected_output in test_get_positive_inputs.
 that:
    actual_output = get_positive(test_input)
    assert actual_output == expected_output, f"Error in getting positive numbers: {test_input} != {expected_output}"

print("All tests passed!")
```