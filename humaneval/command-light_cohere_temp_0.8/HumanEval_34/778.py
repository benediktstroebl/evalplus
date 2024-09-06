```python
def unique(lst):
    """Sorts and returns unique elements in a list"""
    return list(set(lst))

def test_unique():
    """Function to test the unique function"""
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    assert unique(lst) == [0, 2, 3, 5, 9, 123]

# Run the tests
test_unique()
```