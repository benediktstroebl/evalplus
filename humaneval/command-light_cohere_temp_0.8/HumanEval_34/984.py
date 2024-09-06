```python
def unique(l: list):
    return list(set(l))

# Test cases
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
assert unique([]) == []
assert unique([1, 1]) == [1]
assert unique([1, 2, 2, 3]) == [1, 2, 3]
assert unique([-1, 2, 3, 4]) == [2, 3]
assert unique([1, 0, 2, 0]) == [0, 2]

```
This script defines a function `unique` that takes a list as an argument and returns a new list with unique elements using the `set` method, which automatically filters duplicates.  The this unique function is then tested with several input lists, and the results are compared against the expected outputs using `assert` statements.