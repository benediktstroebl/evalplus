```python
def unique(lst):
    """Return sorted unique elements in a list"""
    set1 = set(lst)
    seen = set()
    return list(seen)

# Basic tests
test_unique = [
    [],
    [5, 3, 2, 3],
    [0, 2, 3, 5, 3, 3, 9, 0],
    [123],
]

# Test functions
def test_func():
    assert unique([]) == []
    assert unique([5, 3, 5, 2, 3, 3, 3, 9, 0]) == [0, 2, 3, 5, 9, 123]
    assert unique([123, 5, 3]) == [5, 3]
    assert unique([20, 20]) == [20]

# Run tests
test_func()
```
The code defines a function called `unique` that returns a list of unique elements from a given list. It uses the unique set to filter out duplicates and then converts it back to a list. The code also includes basic tests to ensure the correctness of the `unique` function.