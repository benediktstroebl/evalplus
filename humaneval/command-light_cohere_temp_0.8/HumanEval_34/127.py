```python
def unique(lst):
    """Return sorted unique elements in a list"""
    set1 = set(lst)
    return list(set1)

# Test case 1: Unique( [5, 3, 5, 2, 3, 3, 9, 0, 123])
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Test case 2: Unique( [5, 3, 2, 3, 'a'])
assert unique([5, 3, 2, 3, 'a']) == ['a']

# Test case 3: Unique(set())
assert unique(set()) == []
```
This code defines a function named `unique`, which aims to return the unique elements of an input list. It utilizes the both the fact to ensure that the returned list is indeed unique, the function creates a set from the input list, and then converts it back to a list, effectively removing duplicates. This script also provides three corresponding test cases to validate the correctness of the unique function.