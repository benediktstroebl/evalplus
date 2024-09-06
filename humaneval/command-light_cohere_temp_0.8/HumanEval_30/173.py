```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test case 1: Passing list with positive and negative numbers
assert(get_positive([2, 5, 6])) == [2, 5, 6]

# Test case 2: Passing list with only negative numbers
assert(get_positive([-1, -4, -5, -6])) == [(-1, -4, -5, -6)]

# Test case 3: Passing list with mixed positive and negative numbers
assert(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123])) == [5, 3, 2, 3, 9, 123]

# Test case 4: Passing list with empty list
assert(get_positive([])) == []
```
The function returns a list with only positive numbers from the input list.