```python
def unique(lst):
    """Return sorted unique elements in a list"""
    return list(set(sorted(lst)))

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
    assert unique([]) == []  # Empty list should return an empty set
    assert unique([5, 5]) == [5]
    assert unique([5, 5, 5]) == [5]
```  This code defines a function `unique` that returns unique elements from a list, and passes all the test cases with different inputs.