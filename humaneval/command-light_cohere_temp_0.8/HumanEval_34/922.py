```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not == float('inf')]

# Test case 1: Single list
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Test case 2: List containing float('inf')
assert unique([5, 3, 5, 2, 3, float('inf'), 9, 0, 123]) == [0, 2, 3, 5, 9, float('inf')]

# Test case 3: List containing duplicates
assert unique([5, 3, 5, 2, 3]) == [2, 3]
```
The provided code defines a function called unique that takes a list as input and returns a new list with unique elements. It uses a the particular set of seen elements to filter out duplicates and return the unique ones. The test cases demonstrate the specific usage of the function. The output of the test cases is also expected.