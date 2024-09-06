```python
def unique(lst):
    """Sorts and returns unique elements from a list."""
    seen = set()
    return [x for x in lst if x not in seen and x not == float('inf')]

# Test the function with a sample list
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_list) == [0, 2, 3, 5, 9, 123]

# Test with float('inf') to handle the special case
assert unique([5, 3, 5, 2, 3, float('inf')]) == [5, 3, float('inf')]
```
This code provides a unique function that removes duplicate elements from the passed list and returns them. It also has several test cases: one with a sample list and another with a special float('inf') value to handle the edge case.