```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function with a list of numbers and a string of symbols
test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, "1", -10]
test_str = "get_positive([-1, 2, -4, 5, 6])"
test_result = get_positive(test_list)
test_result_str = "List of positive numbers: " + str(test_result)

# Print the test results
print(test_result_str)
print("Test string:", test_str)
```