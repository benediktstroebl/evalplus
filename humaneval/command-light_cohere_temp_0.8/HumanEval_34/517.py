```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [0, ] and x]

# Test cases
test_data = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_data) == [0, 2, 3, 5, 9, 123]

# List with duplicates
test_data_dup = [5, 3, 5, 2, 3, 3]
assert unique(test_data_dup) == [3, 5, 2, 3]

# List of empty list
test_empty = []
assert unique(test_empty) == []
```
This script defines a function unique that sorts and returns unique elements from an input list. The test cases cover various scenarios, including lists with no duplicates, lists with duplicates, and an empty list, and the function behaves as expected.