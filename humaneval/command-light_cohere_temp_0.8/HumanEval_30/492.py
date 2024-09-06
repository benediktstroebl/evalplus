```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test the function with various lists of numbers
# Ensure it returns the expected list of positive numbers

# Lists to test:
test_lists = [
    [-1, 2, -4, 5],
    [5, 3, -5, 2, -3, 3],
    [5, 0, 123, 1],
    [-10]
]

for test_list in test_lists:
    actual_list = get_positive(test_list)
    assert actual_list == [2, 5, 6, 3, 9, 123, 1]
```
This script defines a function `get_positive` that returns a list of positive numbers from an input list. The function is then tested with various lists of numbers, and the test suite ensures that the expected output is `[2, 5, 6, 3, 9, 123, 1]`.