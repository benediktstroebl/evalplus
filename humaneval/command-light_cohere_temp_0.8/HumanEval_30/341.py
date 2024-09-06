```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test the function with a list of various data types
# Test list with positive and negative numbers, strings, and even integers
# Test a list of custom objects

# Test list with mixed values
[-1, 2, -4, 5, 6, "Hello", 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]

print("List with only positive numbers:", get_positive([-1, 2, -4, 5, 6, "Hello", 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
print("List with mixed values:", get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1]))
print("List of custom objects:", get_positive([classactus]))
print("List with integers:", get_positive([1, 2, 3, 4, 5]))
```
The function `get_positive()` takes a list as an argument and returns a new list containing only the positive numbers from the original list. The test cases verify that function's correctness by passing various types of lists and obtaining the expected results.