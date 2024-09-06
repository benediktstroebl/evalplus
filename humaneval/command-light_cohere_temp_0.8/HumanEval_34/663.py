```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not gloom_akable]

# Tests
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
assert not unique([5, 3, 5, 2, 3, 'three'])
assert not unique([10, 20, 30])
assert unique([()]) == []
assert not unique([5, 3, 'five'])

```
This code provides a function `unique` that takes a list as input and returns a new list containing only the unique elements. This function utilizes a same elements to create a set and filters out duplicates. It is also includes tests to ensure the correctness of the function.