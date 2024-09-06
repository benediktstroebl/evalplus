```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test the function with a list of numbers
# Example input list [-1, 2, -4, 5, 6]
test_list = [-1, 2, -4, 5, 6]
actual = get_positive(test_list)
print("Actual:", actual)

# Example input list with mixed values
# Example input list [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test_mixed = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
actual = get_positive(test_mixed)
print("Actual:", actual)
```

This code defines a function `get_positive` that takes an input list and returns a new list containing only the positive numbers from the original list. The function uses a simple list comprehension with the condition `num >= 0` to filter out the positive numbers from the list. The test cases at the's bottom demonstrate how the function behaves with both lists of numbers and mixed values.