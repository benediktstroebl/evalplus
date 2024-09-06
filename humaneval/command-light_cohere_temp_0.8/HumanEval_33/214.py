```python
def sort_third(lst):
    """Sorts a list l such that values not divisible by three are at front, and the rest are in order."""
    lst[::3] = lst[::3].sort()
    return lst

# Test cases
test_list = [1, 2, 3, 5, 6, 8, 9]
print(sort_third(test_list))  # Expected: [1, 2, 3], [5, 6, 8, 9]

test_list2 = [5, 6, 3, 4, 8, 9, 2]
print(sort_third(test_list2))  # Expected: [2, 6, 3, 4, 8, 9, 5]
```

This script defines a function sort_third that takes a list lst as input and sorts it such that values not divisible by three are at the front and the rest are in order. It achieves this by first moving the the first three elements to the front using slicing and sorting, and then using the slice notation to populate the rest of the list with the sorted values of the first three elements.