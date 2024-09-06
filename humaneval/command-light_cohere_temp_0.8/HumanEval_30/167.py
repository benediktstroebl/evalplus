```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test the function with some inputs
test_get_positive = []
test_get_positive.add([list([-1, 2, -4, 5, 6])]
test_get_positive.add([list([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])]

print(f"Test Results:\n{test_get_positive}")
```
The function get_positive takes a list as an argument and returns a new list containing only the positive numbers from the original list. This function helps by iterating over the list elements and using the condition if num >= 0, which checks if the number is greater than or equal to zero, to only include the positive numbers in the output list.