```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x notlr in [0, None]]

# Test case 1
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Test case 2
assert unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4]

# Test case 3
assert unique([]) == []

# Test case 4
assert unique([5, 3, 'three', 5]) == [5, 3]
```
This script defines a function called unique that takes a list as input and returns a new list with unique elements. The function uses a 'set()' to keep track of elements already seen and then creates a new list with elements not in the seen set. The test cases cover various scenarios to validate the functionality of the unique function.