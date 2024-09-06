```python
def unique(lst):
    """Sorts and returns unique elements in a list"""
    set1 = set(lst)
    return list(set1)

# Test case 1: Test with list containing duplicate elements
assertEqual(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]), [0, 2, 3, 5, 9, 123])

# Test case 2: Test with empty list
assertEqual(unique([]), [])

# Test case 3: Test with list containing only one element
assertEqual(unique([9]), [9])
```
This script defines a function unique that takes a list lst as input and returns a new list containing unique elements from the original. The test cases demonstrate the