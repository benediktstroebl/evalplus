```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test the function with a list of various values
test_list = [
    [-1, 2, -4, 5, 6],
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
]

# Call the function and compare the results with the test list
actual_result = get_positive(test_list)
test_result = [
    [2, 5, 6],
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1],
]

# Print the results for verification
print("Actual Result:", actual_result)
print("Test Result:", test_result)
```