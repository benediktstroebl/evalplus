```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l]

# Test the function with some examples
list1 = [1, 2, 3]
assert incr_list(list1) == [2, 3, 4]

list2 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert incr_list(list2) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Test with a nested list
list3 = [[1, 2, 3], [4, 5, 6]]
assert incr_list(list3) == [[2, 3, 4], [5, 6, 7]]
```