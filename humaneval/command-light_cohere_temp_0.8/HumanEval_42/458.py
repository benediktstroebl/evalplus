```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    new_list = [x + 1 for x in l]
    return new_list

#Test cases
assert incr_list([1, 2, 3]) == [2, 3, 4]

assert incr_list([5, 3, 5]) == [6, 5, 6]

assert incr_list([5, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

assert not [x for x in range(10)] == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

assert list(map(incr_list, [1, 2, 3, 4, 5])) == [2, 3, 4, 6]
```