Here is a self-contained Python script that defines a function unique which returns sorted unique elements in a list:
```python
def unique(lst):
    """Return sorted unique elements in a list"""
    return sorted(set(lst))

# Test cases
def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```

Feel and test_unique() function to ensure that the unique() function behaves as expected, which passes all the test cases.