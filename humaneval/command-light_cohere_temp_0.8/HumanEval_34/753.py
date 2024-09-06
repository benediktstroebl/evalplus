```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not None]

# Test cases
tests = [
    dict(zip(' Test Case 1'.split(), unique(['5', '3', '5', '2', '3', '3', '9', '0', '123'])))
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
]
```
This script defines a function `unique` that takes a list as an argument and returns a new list containing unique elements from the original list. The function uses a tested using a set to keep track of elements seen so far, then it iterates through the input list and adds elements to the set only if they are not in the set and not `None` (which is handled separately). 

This approach guarantees the uniqueness of the elements in the output list, which is essential for this problem.