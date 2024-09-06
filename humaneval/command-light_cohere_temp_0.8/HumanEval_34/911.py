Here is a self-contained Python function that solves the problem of finding unique elements in a list:
```python
def unique(lst):
    return list(set(lst))

# Test case 1: Verify function works with list of numbers
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Test case 2: Verify function works with list of strings
assert unique(["a", "b", "c", "d"]) == ["a", "b", "c", "d"]

# Test case 3: Remove duplicates from a list of mixed types
assert unique([5, 3, 7, 2, 6, 1, 8]) == [5, 3, 7, 2, 6]
```
This script defines a function unique that takes a list as input and returns a new list containing only the unique elements from the original list. The test cases demonstrate the