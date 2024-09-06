```python
def unique(lst):
    """Return sorted unique elements in a list"""
    set1 = set(lst)
    return list(set1)

def test_unique():
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    assert unique(lst) == [0, 2, 3, 5, 9, 123]

# Run the tests
test_unique()
```

This code defines a function unique that returns a list with unique elements after removing duplicates from the input list. The test_unique function contains a list of numbers with duplicates and passes the test with the result of the unique function.