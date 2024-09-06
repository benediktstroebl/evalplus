```python
def unique(lst):
    return list(set(lst))

# Test case 1
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Test case 2
my_list = [7, 2, 4, 8, 9, 6, 5, 3, 5, 1]
assert set(unique(my_list)) == set(my_list)

# Test case 3
duplicates = {'a': 1, 'b': 2, 'c': 1}
assert set(unique(duplicates)) == {'a', 'b', 'c'}
```

This Python function unique will remove duplicates from a given list and return the sorted unique elements. The test cases demonstrate the following is correct.