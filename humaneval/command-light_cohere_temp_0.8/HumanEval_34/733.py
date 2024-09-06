```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [0, ]]

# Test case 1
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Test case 2
assert unique([]) == []

# Test case 3
assert unique([-1]) == []

# Test case 4
assert unique([1, 2, 3, 4, 5]) == [1, 2, 3]

# Test case 5 (Using set as input)
assert unique(set([5, 3, 5, 2, 3, 3, 9, 0, 123])) == [0, 2, 3, 5, 9, 123]
```
This code defines a unique function that takes a list as input and uses a set to track the unique elements in the list. It then returns theole list of the unique elements. The test cases are used to validate the `unique` function.