```python
def unique(lst):
    """Return sorted unique elements in a list"""
    set1 = set(lst)
    return list(set1)

# Test cases
def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

if __name__ == "__main__":
    # Test suite execution
    test_unique()
```
The provided Python script defines a function unique that takes a list lst as input and returns a new list containing unique elements from the original list. This is unique set of elements is achieved using the set() function to convert the list into a set, and the list() function to convert the set back to a list.

The script also includes a test case with several test data points. When the script is run, the test suite is executed, and the results are compared against the expected values.