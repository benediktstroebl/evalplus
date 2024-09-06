```python
def unique(l: list):
    return list(set(l))

# Test case 1: Verify function correctly returns unique elements
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Test case 2: Ensure duplicates are also correctly removed
assert unique([1, 2, 3, 3, 4, 5]) == [1, 2, 3, 4]
```

This script defines a function unique that takes a list as an argument and returns a new list containing only the unique elements. It is the using the the set() function to create a set from the input list, and then convert it back to a list to get the unique elements.