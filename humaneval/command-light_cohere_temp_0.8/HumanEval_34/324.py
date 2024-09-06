Here is a self-contained Python script that provides a function to get unique elements from a list:
```python
def unique(lst):
    set(lst)  # Convert list to set
    return list(set())

# Test suite
def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

test_unique()
```

This script provides a unique() function that converts the input list into a set and then back into a list, ensuring that duplicates are eliminated. It also has a test suite to validate the functionality of the unique() function with a set of sample inputs.