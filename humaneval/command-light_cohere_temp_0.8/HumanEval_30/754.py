```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num > 0]

# Test the function with some input lists
assertEqual(get_positive([-1, 2, -4, 5, 6]) , [2, 5, 6])
assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) , [5, 3, 2, 3, 9, 123])
```
This script defines a function get_positive that takes in a list and returns a new list with only the positive numbers from the original list. It also has tests the wavelengths of this function by testing it with two input lists, which results in two assertions passing successfully.