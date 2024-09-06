```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    new_list = [x + 1 for x in l]
    return new_list

#Test cases
assert incr_list([1, 2, 3]) == [2, 3, 4]

assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

assert not listsEqual(incr_list([1, 2, 3]), incr_list([1, 2, 3]))

def listsEqual(test_list, ref_list):
    """Check if two lists are equal"""
    return all(test_list == ref_list)
```