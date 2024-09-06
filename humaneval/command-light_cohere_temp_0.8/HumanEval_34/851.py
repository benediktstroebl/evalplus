```python
def unique(lst):
    """Return sorted unique elements in a list"""
    return list(set(sorted(lst)))

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```
This code defines a function `unique` that takes a list as an argument and returns a new list containing the unique elements of the original list. The `test_unique` function tests the output of the `unique` function with a sample list and asserts that the output is correct.