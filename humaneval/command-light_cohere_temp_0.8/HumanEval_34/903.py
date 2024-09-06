Here is a self-contained Python script that solves the problem of sorting unique elements in a list:

```python
def unique(lst):
    """Return sorted unique elements in a list"""
    return sorted(set(lst))

# Test case 1: Check if unique function works correctly with list of numbers
test_unique = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
assert test_unique == [0, 2, 3, 5, 9, 123]

# Test case 2: Check with list of strings
test_strings = unique(["Hello", "World", "!!!"])
assert test_strings == ["Hello", "World", "!!!"]
```

This script defines a function `unique` that takes a list as input and returns a new list containing only the unique elements from the original list. This function uses the simple set() function to filter out duplicates and return the unique elements in sorted order.

The script also provides two test cases to check if the `unique` function is working correctly with different types of lists.

Please feel free to use this code for your specific problem and modify it further if needed!