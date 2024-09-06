```python
def unique(lst):
    return sorted(set(lst))

# Test case 1:
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Test case 2:
assert unique([5, 3, 'three', 5, 'five']) == ['five', 'three', 'five']

# Test case 3:
assert unique([]) == []
```
This script defines a function called `unique` that takes a list as an argument and returns a sorted unique elements of that list. The function uses the unique elements using the set function and the sort function to create a unique set of elements, which are then sorted into a new list.