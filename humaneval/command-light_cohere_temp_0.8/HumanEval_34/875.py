```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not None]

# Test cases
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_list) == [0, 2, 3, 5, 9, 123]

test_empty = []
assert unique(test_empty) == []

test_null = None
assert unique(test_null) == []
```
The provided code defines a function `unique` that returns a list of unique elements from the input list `lst`. The function utilizes a set called `seen` to track encountered elements. The function iterates over the only elements that are not in the `seen` set and are not `None` are added to the returned list.