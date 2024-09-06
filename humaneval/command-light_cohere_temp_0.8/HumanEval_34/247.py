```python
def unique(lst):
    """Return sorted unique elements in a list"""
    return list(set(sorted(lst)))

# Test suite:
def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```  This code defines a function unique that takes a list lst as input and returns a new list containing the unique elements from the original list, after sorting them in ascending order. The test_unique function tests whether the unique function with a sample list and checks if the result matches the expected output.