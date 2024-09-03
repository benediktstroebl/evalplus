```python
def next_smallest(lst):
    """
    Returns the next smallest element of the list.
    """
    Requires a list of integers.
    if len(lst) == 0:
        return None
    if lst[0] < lst[1]:
        return lst[1]
    else:
        return lst[0]

# Tests
assert next_smallest([1, 2, 3, 4, 5]) == 2
assert next_smallest([5, 1, 4, 3, 2]) == 2
assert next_smallest([]) == None
assert next_smallest([1, 1]) == None
```