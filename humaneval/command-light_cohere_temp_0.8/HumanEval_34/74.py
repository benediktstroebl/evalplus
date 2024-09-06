```python
def unique(lst):
    return list(set(lst))

# Test suite for unique function
def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Driver code to run the test suite
test_unique()
```

This code defines a function unique that returns a list of unique elements from the input list lst, using the set() function and list conversion. The test suite test_unique() contains a single assertion that checks the result of calling unique on a sample list, and passes the test. This demonstrates the covered code that checks the expected output for the unique function.