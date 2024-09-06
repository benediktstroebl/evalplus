```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not in []]

# Test case 1
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Test case 2
assert unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4]

# Test case 3
assert unique([1, 2, 3, 4, 5, 6]) == [1, 2, 3]
```
The function unique is designed to take a list as input and produce a new list containing only the unique elements from the original list. The function uses a simple set seen to keep track of unique elements. The set contains all elements from the list that are not in the set and are not in [] (empty list). The function then returns a new list containing only these unique elements.