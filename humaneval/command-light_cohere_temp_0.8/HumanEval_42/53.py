```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

#Test case 1
assert incr_list([1, 2, 3]) == [2, 3, 4]

#Test case 2
assert incr_list([5, 3, 5]) == [6, 5, 6]

#Test case 3
assert incr_list([5, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

#Test case 4
l = [0, 1, 2]
new_val = incr_list(l)
assert len(new_val) == 3
assert all(map(lambda x: x+1, l)) == map(lambda x: x+1, new_val)
```