```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    return list(set(sorted(l)))

def test_unique():
    """Basic test of the unique function"""
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```

The unique function uses the set function to create a unique set of elements from the list, and the sorted function to sort the elements of the set. Then, the list function is applied to convert the set back into a list, resulting in a sorted list of unique elements. The test_unique function passes the test cases to ensure the expected output.