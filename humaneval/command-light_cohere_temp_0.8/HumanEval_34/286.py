```python
def unique(lst):
    """Return sorted unique elements in a list"""
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, ""]]

# Tests
def test_unique():
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    assert unique(lst) == [0, 2, 3, 5, 9, 123]
```
The above code defines a function unique that takes a list lst as an argument and returns a new list with unique elements from the original list. The function uses a simple logic to check if an element exists in the set seen before, and then returns that element if not present. The test_unique function tests the result with the given list.